import cv2
import time
import os

# create folders if not exist
os.makedirs("snapshots", exist_ok=True)
os.makedirs("logs", exist_ok=True)

def save_snapshot(frame):
    filename = f"snapshots/{int(time.time())}.jpg"
    cv2.imwrite(filename, frame)

def log_event(event):
    with open("logs/events.txt", "a") as f:
        f.write(event + "\n")