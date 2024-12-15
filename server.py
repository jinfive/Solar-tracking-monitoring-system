from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import socket
import json
import threading
import sqlite3
from datetime import datetime
import re

app = Flask(__name__)
socketio = SocketIO(app)
UDP_IP = '0.0.0.0'
UDP_PORT = 8080
DB_FILE = 'energy_data.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history', methods=['GET'])
def history():
    # 날짜 형식 변환 함수
    def format_date(date_str):
        if date_str:
            # '오전/오후'를 AM/PM으로 변경
            date_str = re.sub(r'오전', 'AM', date_str)
            date_str = re.sub(r'오후', 'PM', date_str)
            # 문자열을 datetime 객체로 변환
            try:
                date_obj = datetime.strptime(date_str, '%m/%d/%Y %I:%M %p')
            except ValueError:
                # 시간 형식이 '%I:%M %p'과 일치하지 않는 경우, 오류를 방지하기 위한 대체 로직
                date_obj = datetime.strptime(date_str, '%m/%d/%Y %H:%M %p')
            # SQLite 형식으로 변환
            return date_obj.strftime('%Y-%m-%d %H:%M:00')
        else:
            # 날짜 파라미터가 없는 경우 현재 날짜 사용
            return datetime.now().strftime('%Y-%m-%d %H:%M:00')

    # 클라이언트로부터 전달받은 시작 및 종료 날짜
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # 날짜 형식 변환 적용
    start_date = format_date(start_date)
    end_date = format_date(end_date)

    # SQLite 데이터베이스에서 해당 기간의 데이터 조회
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT device_id, power_value, timestamp FROM energy_data
        WHERE timestamp BETWEEN ? AND ?
        ORDER BY timestamp
    ''', (start_date, end_date))

    data = cursor.fetchall()
    conn.close()

    # 조회된 데이터를 JSON 형식으로 변환
    json_data = [{"device_id": device_id, "power_value": power_value, "timestamp": timestamp} for device_id, power_value, timestamp in data]

    if request.args.get('start_date'):
        # AJAX 요청에 대한 응답
        return jsonify(json_data)
    else:
        # 페이지 최초 로드에 대한 응답
        return render_template('history.html', initial_data=json_data, current_date=start_date)


# 데이터베이스 초기화 함수
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS energy_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device_type TEXT,
                device_id TEXT,
                power_value REAL,
                timestamp DATETIME
            )
        ''')

# 데이터베이스에 데이터 저장
def save_data(device_type, device_id, power_value):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO energy_data (device_type, device_id, power_value, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (device_type, device_id, power_value, datetime.now().strftime('%Y-%m-%d %H:%M:00')))
        conn.commit()

def start_udp_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket.bind((UDP_IP, UDP_PORT))

    last_minute = datetime.now().minute
    data_buffer = {}

    while True:
        data, _ = udp_socket.recvfrom(1024)
        try:
            sensor_data = json.loads(data.decode())

            # 수신된 데이터를 콘솔에 출력
            print(f"Received data: {sensor_data}")

            current_minute = datetime.now().minute
            device_id = sensor_data['device_id']
            device_type = sensor_data['device_type']
            power_value = sensor_data['power_value']

            # 현재 분이 바뀌었을 경우 저장
            if current_minute != last_minute:
                for device in data_buffer:
                    save_data(data_buffer[device]['device_type'], device, data_buffer[device]['power_value'])
                data_buffer.clear()
                last_minute = current_minute

            # 데이터 버퍼에 저장
            data_buffer[device_id] = {'device_type': device_type, 'power_value': power_value}

            socketio.emit('newdata', sensor_data)
        except json.JSONDecodeError:
            pass

if __name__ == '__main__':
    init_db()
    udp_thread = threading.Thread(target=start_udp_server)
    udp_thread.start()
    socketio.run(app, host='0.0.0.0', port=5000)