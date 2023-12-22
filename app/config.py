import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def get_secret(key, json_path: str = str(BASE_DIR / "secrets.json")):
    with open(json_path) as file:
        secrets = json.loads(file.read())
        try:
            return secrets[key]
        except ():
            raise EnvironmentError(f"There is not {key} in file")


DB_NAME = get_secret("DB_NAME")
DB_URL = get_secret("DB_URL")
