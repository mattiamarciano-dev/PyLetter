import datetime

class TimeGetter:
    @staticmethod
    def get_current_hour():
        return datetime.datetime.now().hour

    @staticmethod
    def get_current_minute():
        return datetime.datetime.now().minute

    @staticmethod
    def get_current_day() -> str:
        return datetime.date.today().isoformat()


    @staticmethod
    def get_current_time_formatted(extense: bool = True) -> str:
        return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") if extense else datetime.datetime.now().strftime("%d/%m/%Y")