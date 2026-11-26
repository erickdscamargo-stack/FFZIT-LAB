
import tempfile
import unittest

from pathlib import Path
from ffzit.storage import LocalStorage


class StorageTests(unittest.TestCase):

    def test_save_and_load(self):

        with tempfile.TemporaryDirectory() as directory:

            storage = LocalStorage(
                Path(directory) / "settings.json"
            )

            settings = {
                "auto_aim_demo": True,
                "esp_demo": False,
                "anticheat_demo": True,
                "difficulty": "hard"
            }

            storage.save(settings)

            loaded = storage.load()

            self.assertTrue(
                loaded["auto_aim_demo"]
            )

            self.assertFalse(
                loaded["esp_demo"]
            )

            self.assertEqual(
                loaded["difficulty"], "hard"
            )

    def test_invalid_setting(self):

        with tempfile.TemporaryDirectory() as directory:

            storage = LocalStorage(
                Path(directory) / "settings.json"
            )

            with self.assertRaises(ValueError):
                storage.save({"unknown": True})


if __name__ == "__main__":
    unittest.main()
  
