
class ESPDemo:

    def __init__(self, arena):
        self.arena = arena
        self.enabled = True

    def scan(self, observer_x, observer_y):
        if not self.enabled:
            return []

        results = []

        for target in self.arena.get_targets():
            distance = self.arena.distance(
                observer_x,
                observer_y,
                target["x"],
                target["y"]
            )

            results.append({
                "id": target["id"],
                "x": target["x"],
                "y": target["y"],
                "distance": round(distance, 2),
                "label": f"TARGET {target['id']}"
            })

        return results
      
