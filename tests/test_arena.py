
import unittest

from ffzit.arena import Arena
from ffzit.aim_trainer import AimTrainer
from ffzit.esp import ESPDemo


class ArenaTests(unittest.TestCase):

    def setUp(self):
        self.arena = Arena(800, 500, 2)

    def test_target_count(self):
        self.assertEqual(
            len(self.arena.get_targets()), 2
        )

    def test_nearest_target(self):
        target = self.arena.get_targets()[0]

        result = self.arena.nearest_target(
            target["x"], target["y"]
        )

        self.assertEqual(
            result["id"], target["id"]
        )

    def test_hit(self):
        target = self.arena.get_targets()[0]

        self.assertTrue(
            self.arena.hit(target["id"])
        )

        self.assertEqual(
            len(self.arena.get_targets()), 1
        )

    def test_aim_selection(self):
        target = self.arena.get_targets()[0]

        aim = AimTrainer(self.arena)
        aim.enable()

        result = aim.update(
            target["x"], target["y"]
        )

        self.assertEqual(
            result["id"], target["id"]
        )

    def test_esp(self):
        esp = ESPDemo(self.arena)

        result = esp.scan(400, 250)

        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()
  
