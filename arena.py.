
import math
import random


class Arena:

    def __init__(self, width=800, height=500, target_count=5):
        self.width = width
        self.height = height
        self.target_count = target_count
        self.targets = []
        self.reset()

    def reset(self):
        self.targets = []

        for index in range(self.target_count):
            self.targets.append({
                "id": index + 1,
                "x": random.uniform(60, self.width - 60),
                "y": random.uniform(60, self.height - 60),
                "alive": True
            })

    def get_targets(self):
        return [
            target.copy()
            for target in self.targets
            if target["alive"]
        ]

    def distance(self, x1, y1, x2, y2):
        return math.hypot(x2 - x1, y2 - y1)

    def nearest_target(self, x, y):
        targets = self.get_targets()

        if not targets:
            return None

        return min(
            targets,
            key=lambda target: self.distance(
                x, y, target["x"], target["y"]
            )
        )

    def hit(self, target_id):
        for target in self.targets:
            if target["id"] == target_id and target["alive"]:
                target["alive"] = False
                return True

        return False
        
