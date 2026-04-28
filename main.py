import cv2
from detector import detect
from tracker import Tracker
from behavior import check_loitering
from utils import save_snapshot, log_event

cap = cv2.VideoCapture("test3.mp4")

tracker = Tracker()

while True:
    ret, frame = cap.read()
    ret, frame = cap.read()

    if not ret:
        print("Reconnecting...")
        break

    boxes = detect(frame)
    objects = tracker.update(boxes)

    for obj_id, (cx, cy) in objects.items():

        # draw box (find matching box)
        for (x1, y1, x2, y2) in boxes:
            if x1 < cx < x2 and y1 < cy < y2:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

        is_loitering, threat = check_loitering(obj_id, (cx, cy))

        # ID label
        cv2.putText(frame, f"ID {obj_id}", (cx, cy-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

        # threat display
        cv2.putText(frame, f"Threat: {threat}%", (cx, cy+15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

        if is_loitering:
            cv2.putText(frame, "LOITERING ALERT!", (cx, cy+35),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

            save_snapshot(frame)
            log_event(f"Loitering detected | ID: {obj_id} | Threat: {threat}%")

    cv2.imshow("Smart CCTV System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()