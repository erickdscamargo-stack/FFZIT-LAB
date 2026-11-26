
class AimTrainer:

    def __init__(self, arena):
        self.arena = arena
        self.enabled = False
        self.selected_target = None
        self.hits = 0

    def enable(self, enabled=True):
        self.enabled = bool(enabled)

    def update(self, crosshair_x, crosshair_y):
        if not self.enabled:
            self.selected_target = None
            return None

        target = self.arena.nearest_target(
            crosshair_x,
            crosshair_y
        )

        self.selected_target = (
            target["id"] if target else None
        )

        return target

    def register_hit(self):
        if self.selected_target is None:
            return False

        if self.arena.hit(self.selected_target):
            self.hits += 1
            self.selected_target = None
            return True

        return False
      
