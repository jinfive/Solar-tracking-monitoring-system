# Solar tracking monitoring system

## index

- [🖼️ project image](#-project-image)
- [📌 project information](#-project-information)
- [👥 Team introduction](#-Team-introduction)
- [🚀 Installation](#-Installation)
- [🌐 etc](#-etc)

## 🖼️ project image
<div align="center">
  <a href="https://ibb.co/4gs1mHzc"><img src="https://i.ibb.co/LhQNk3mM/Kakao-Talk-Photo-2025-02-09-21-14-43-002.jpg" alt="Kakao-Talk-Photo-2025-02-09-21-14-43-002" border="0"></a>
  
  <a href="https://ibb.co/tTY48YX0"><img src="https://i.ibb.co/Pv1Nw1Q2/Kakao-Talk-Photo-2025-02-09-21-14-43-001.jpg" alt="Kakao-Talk-Photo-2025-02-09-21-14-43-001" border="0"></a>
  <br>
  
</div>



## Repository visits
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fjinfive%2FNewProject1&count_bg=%2379C83D&title_bg=%23555555&icon=java.svg&icon_color=%23D7C7C7&title=hits&edge_flat=false"/></a>

## 📌 project information
### KANGWON NATIONAL UNIVERSITY
📖 
Development period:2023.11.09 ~ 2023.12.07
<br>
## 👥 Team introduction
Team leader:김진오
<br>
team member:남강현,박상욱,이정원

## Project Introduction
Development of Solar tracking monitoring system
<ul>
  <li>Automated sun position tracking for optimal panel alignment</li>
  <li>Enhanced energy capture through dynamic positioning</li>
  <li>Real-time power generation data collection and analysis</li>
  <li>Historical data tracking with customizable date ranges</li>
</ul>
<br>
<h2>Getting Started Guide</h2> 

Requirement
--
<ul>
  <h3>Hardware Components</h3>
<li>🌞 Solar Panel with INA219 Current Sensor</li>
<li>🔌 Additional INA219 Current Sensor</li>
<li>📡 ESP8266 Microcontroller</li>
<li>🥧 Raspberry Pi (for system control)</li>
<li>🎛️ ADS1115 ADC Module</li>
<h3>Software Dependencies</h3> 
<li>🐍 Python 3.13.0</li>
<li>🌐 HTML5</li>
<li>💾 SQLite</li>
  
</ul>


## 🚀 Installation
--

```
git clone https://github.com/jinfive/Power-analysis-control-system-for-home-smart-grid.git
```

```
cd /path/to/script/directory
python3 four_ver_rpi.py
```
Run script automatically when Raspberry Pi boots
```
nano launcher.sh
```
Enter the following
```
#!/bin/sh
cd /path/to/script/directory
python3 four_ver_rpi.py
```

```
chmod 755 launcher.sh
```

Edit crontab

```
sudo crontab -e
```
Add the following line to the end of the file

```
@reboot sh /path/to/launcher.sh &
```
## STACK 😸
<br>
Enviroment
<br>
<div style="display: flex; align-items: center;">
  <img src="https://img.shields.io/badge/raspberrypi-A22846?style=for-the-badge&logo=raspberrypi&logoColor=black" style="border-radius:10px">
  <img src="https://img.shields.io/badge/googlecolab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white" style="border-radius:10px">
  
</div>
<br><br>
Development
<br>
<div style="display: flex; align-items: center;">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white" style="border-radius:10px">
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white" style="border-radius:10px">
  
</div>

<br><br>
Communication
<br>
<div style="display: flex; align-items: center;">
  <img src="https://img.shields.io/badge/kakaotalk-FFCD00?style=for-the-badge&logo=kakaotalk&logoColor=white" style="border-radius:10px">
</div>


## 🌐 etc
<a href="https://docs.google.com/spreadsheets/d/1SN1DLJhe6vC6NH8kIV9UJla5Z8VHP_Rl/edit?gid=429682832#gid=429682832" target="_blank">grades data >> https://docs.google.com/spreadsheets/d/1SN1DLJhe6vC6NH8kIV9UJla5Z8VHP_Rl/edit?gid=429682832#gid=429682832</a>

<a href="https://drive.google.com/file/d/1fBGJxnjC3L75YPvUwr9KR8rwJBDAOmsQ/view?usp=sharing" target="_blank">presentation >> https://drive.google.com/file/d/1fBGJxnjC3L75YPvUwr9KR8rwJBDAOmsQ/view?usp=sharing</a>

<a href="https://drive.google.com/file/d/1QAvmrWZJEv4rtOqb98qd1T-YY2MO6o6d/view?usp=sharing" target="_blank">final repot>> https://drive.google.com/file/d/1QAvmrWZJEv4rtOqb98qd1T-YY2MO6o6d/view?usp=sharing</a>
](https://drive.google.com/file/d/1fBGJxnjC3L75YPvUwr9KR8rwJBDAOmsQ/view?usp=sharing)
