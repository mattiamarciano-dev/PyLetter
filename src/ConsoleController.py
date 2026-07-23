from rich.console import Console
from rich.table import Table
from rich import box
from User import User

class ConsoleController:
    @staticmethod
    def show_users_table(users: list[User]) -> None:
        console = Console()
        table = Table(title = "USERS", box = box.SIMPLE)
        table.add_column("INDEX")
        table.add_column("ID")
        table.add_column("EMAIL")
        table.add_column("HOUR")
        table.add_column("CATEGORY")
        table.add_column("LAST SENT")
        for index, user in enumerate(users):
            table.add_row(str(index), user.id, user.email, str(user.hour), user.news_category.name, user.last_sent)
        console.print(table)