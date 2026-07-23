from PathGetter import PathGetter
from TimeGetter import TimeGetter

class Logger:
    @staticmethod
    def print(content: str) -> None:
        print(f"{TimeGetter.get_current_time_formatted()} - {content}")
    
    @staticmethod
    def print_interruption() -> None:
        print()
        print("-" * 50)
        print()

    @staticmethod
    def log(content: str) -> None:
        logs_path = PathGetter.get_logs_path()
        with open(f"{logs_path}/{TimeGetter.get_current_day()}", 'a') as f:
            f.write(f"{TimeGetter.get_current_time_formatted()} - {content}\n")