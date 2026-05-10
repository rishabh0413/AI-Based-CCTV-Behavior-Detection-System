# AI-Based CCTV Behavior Detection System

This project is a real-time surveillance system that detects suspicious human behavior such as loitering using computer vision techniques.

## Features
- Real-time person detection using YOLOv8
- Object tracking with unique IDs
- Loitering detection using time + movement analysis
- Threat level scoring
- Automatic snapshot capture
- Event logging system

## Tech Stack
- Python
- OpenCV
- YOLO (Ultralytics)
- NumPy, SciPy

## Input Options
- Webcam
- Mobile camera (DroidCam)
- Pre-recorded CCTV video

## Use Cases
- Smart surveillance systems
- Security monitoring
- Behavior analysis

## How to Run

```bash
pip install -r requirements.txt
python main.py
