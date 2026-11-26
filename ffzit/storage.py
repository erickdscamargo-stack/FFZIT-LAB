
import json
from pathlib import Path

DEFAULT_SETTINGS = {
    "auto_aim_demo": False,
    "esp_demo": True,
    "anticheat_demo": True,
    "difficulty": "normal"
}


class LocalStorage:

    def __init__(self, filename):
        self.path = Path(filename)

    def load(self):
        if not self.path.exists():
            return DEFAULT_SETTINGS.copy()

        try:
            data = json.loads(
                self.path.read_text(encoding="utf-8")
            )

            if not isinstance(data, dict):
                return DEFAULT_SETTINGS.copy()

            result = DEFAULT_SETTINGS.copy()
            result.update(data)

            return result

        except (OSError, ValueError):
            return DEFAULT_SETTINGS.copy()

    def save(self, settings):
        if not isinstance(settings, dict):
            raise ValueError("Configurações inválidas")

        if set(settings) - set(DEFAULT_SETTINGS):
            raise ValueError("Configuração desconhecida")

        result = DEFAULT_SETTINGS.copy()
        result.update(settings)

        for key in (
            "auto_aim_demo",
            "esp_demo",
            "anticheat_demo"
        ):
            if type(result[key]) is not bool:
                raise ValueError("Valor booleano inválido")

        if result["difficulty"] not in (
            "easy", "normal", "hard"
        ):
            raise ValueError("Dificuldade inválida")

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        temporary = self.path.with_suffix(".tmp")

        temporary.write_text(
            json.dumps(result, indent=4),
            encoding="utf-8"
        )

        temporary.replace(self.path)

        return result
      
