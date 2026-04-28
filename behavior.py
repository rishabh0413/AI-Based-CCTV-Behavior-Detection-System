import time

loitering_data = {}

def check_loitering(object_id, position):
    current_time = time.time()

    if object_id not in loitering_data:
        loitering_data[object_id] = {
            "start_time": current_time,
            "positions": [position],
            "alerted": False
        }
        return False, 0

    data = loitering_data[object_id]
    data["positions"].append(position)

    # movement calculation
    xs = [p[0] for p in data["positions"]]
    ys = [p[1] for p in data["positions"]]

    movement = (max(xs) - min(xs)) + (max(ys) - min(ys))
    duration = current_time - data["start_time"]

    # threat score
    threat = min(100, int(duration * 5))

    if duration > 10 and movement < 50:
        if not data["alerted"]:
            data["alerted"] = True
            return True, threat

    return False, threat