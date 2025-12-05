# 🤖 Pravega 2025 - Robotics Competition Technical Reports

Technical reports and CAD documentation for IISc Bangalore's Pravega 2025 robotics competitions.

**Team:** amiarinjaysarkar  
**Institution:** Jadavpur University  
**Competition:** Pravega 2025 @ IISc Bangalore

---

## 👥 Team Members

| Name | Role | Contact |
|------|------|---------|
| **Arinjay Sarkar** | Team Leader | +91 7003828489 |
| **Saptarshi Nanda** | Member | +91 8617471550 |
| **Soureen Majumder** | Member | +91 9123779351 |

---

## 📁 Repository Structure

```
Pravega2025-Robotics/
├── LineMazeFollower/          # Line Maze Follower Robot
│   ├── images/                # Robot photos
│   ├── cad/                   # CAD drawings
│   ├── index.html             # Technical Report (HTML)
│   └── Technical_Report_Final.pdf
│
├── PickDrop/                  # Pick & Drop Robot
│   ├── images/                # Generated diagrams
│   ├── index.html             # Technical Report (HTML)
│   └── PickDrop_Report_v3.pdf
│
├── RoboSprint/                # Robo Sprint Robot
│   ├── images/                # Generated diagrams
│   ├── index.html             # Technical Report (HTML)
│   └── RoboSprint_Technical_Report.pdf
│
├── TugOfWar/                  # Tug of War Robot
│   ├── images/                # Generated diagrams
│   ├── index.html             # Technical Report (HTML)
│   └── TugOfWar_Technical_Report.pdf
│
├── .gitignore
└── README.md
```

---

## 🏆 Competitions

### 1. Line Maze Follower
**Tagline:** Navigate the maze, conquer the lines.

An autonomous robot that follows black lines on white surface, navigating complex mazes with T-junctions, X-junctions, and dead ends.

- **Sensors:** 5-channel IR sensor array
- **Controller:** Arduino Uno
- **Drive:** Differential drive with BO motors

### 2. Pick & Drop
**Tagline:** Grip. Lift. Deliver.

A pick-and-place robot that identifies, picks up, and accurately places objects into designated target zones.

- **Mechanism:** Servo-actuated parallel jaw gripper
- **Sensors:** Ultrasonic + IR for object detection
- **Controller:** Arduino Mega

### 3. Robo Sprint
**Tagline:** Every millisecond counts.

A high-speed obstacle course robot navigating ramps, tunnels, and speed breakers.

- **Features:** 4WD with suspension system
- **Sensors:** Ultrasonic + IMU for stability
- **Control:** Remote + semi-autonomous modes

### 4. Tug of War
**Tagline:** Pull harder. Think smarter.

A high-torque robot designed to outpull opponents in head-to-head elimination rounds.

- **Motors:** 775 DC with 100:1 gear reduction
- **Features:** Anti-slip control, burst mode
- **Drivers:** BTS7960 high-current drivers (43A)

---

## 📜 License

This project is for educational and competition purposes.

---

*Made with ❤️ by Team amiarinjaysarkar - Jadavpur University*
