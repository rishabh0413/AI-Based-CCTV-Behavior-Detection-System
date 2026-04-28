import numpy as np
from scipy.spatial import distance

class Tracker:
    def __init__(self):
        self.objects = {}
        self.id_count = 0

    def update(self, boxes):
        new_objects = {}

        centroids = []
        for box in boxes:
            x1, y1, x2, y2 = box
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            centroids.append((cx, cy))
import numpy as np
from scipy.spatial import distance

class Tracker:
    def __init__(self):
        self.objects = {}
        self.id_count = 0

    def update(self, boxes):
        new_objects = {}

        centroids = []
        for box in boxes:
            x1, y1, x2, y2 = box
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            centroids.append((cx, cy))

        if len(self.objects) == 0:
            for c in centroids:
                self.objects[self.id_count] = c
                self.id_count += 1
        else:
            object_ids = list(self.objects.keys())
            object_centroids = list(self.objects.values())

            D = distance.cdist(object_centroids, centroids)

            used = set()

            for i in range(len(object_ids)):
                min_index = np.argmin(D[i])

                if min_index not in used:
                    self.objects[object_ids[i]] = centroids[min_index]
                    used.add(min_index)

        return self.objects
        if len(self.objects) == 0:
            for c in centroids:
                self.objects[self.id_count] = c
                self.id_count += 1
        else:
            object_ids = list(self.objects.keys())
            object_centroids = list(self.objects.values())

            D = distance.cdist(object_centroids, centroids)

            for i in range(len(object_ids)):
                min_index = np.argmin(D[i])
                self.objects[object_ids[i]] = centroids[min_index]

        return self.objects