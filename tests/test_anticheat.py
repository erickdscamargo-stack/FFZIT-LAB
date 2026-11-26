
import unittest

from ffzit.anticheat import AntiCheatDemo


class AntiCheatTests(unittest.TestCase):

    def test_normal_movement(self):
        detector = AntiCheatDemo(500)

        detector.analyze("player", 0, 0, 1)

        result = detector.analyze(
            "player", 10, 0, 2
        )

        self.assertFalse(result["suspicious"])

    def test_suspicious_movement(self):
        detector = AntiCheatDemo(100)

        detector.analyze("player", 0, 0, 1)

        result = detector.analyze(
            "player", 1000, 0, 2
        )

        self.assertTrue(result["suspicious"])

    def test_repeated_timestamp(self):
        detector = AntiCheatDemo()

        detector.analyze("player", 0, 0, 1)

        result = detector.analyze(
            "player", 10, 0, 1
        )

        self.assertTrue(result["suspicious"])


if __name__ == "__main__":
    unittest.main()
  
