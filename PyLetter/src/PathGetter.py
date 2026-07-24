import os
from pathlib import Path

class PathGetter:

    @staticmethod
    def get_logs_path() -> Path:
        base_dir = Path(__file__).resolve().parent.parent
        return base_dir / "logs"

    @staticmethod
    def get_database_path() -> str:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_dir, "database", "database.db")