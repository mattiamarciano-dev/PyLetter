from DataBaseManager import DataBaseManager
from EmailSender import EmailSender
from NewsGetter import NewsGetter
from TimeGetter import TimeGetter
from Email import Email
from ContentFormatter import ContentFormatter
from ConsoleController import ConsoleController
from User import User
from Logger import Logger

import time
import os
from dotenv import load_dotenv

load_dotenv()

class NewsLetter:
    users: list[User]

    def main(self) -> None:
        sender = os.getenv("SENDER")
        key = os.getenv("APIKEY")
        mail_password = os.getenv("EMAIL_PASSWORD")
        
        Logger.print("SENDER FOUND" if sender else "SENDER NOT FOUND PLEASE CHECK .ENV FILE")
        Logger.log("SENDER FOUND" if sender else "SENDER NOT FOUND PLEASE CHECK .ENV FILE")
        Logger.print("APIKEY FOUND" if key else "APIKEY NOT FOUND PLEASE CHECK .ENV FILE")
        Logger.log("APIKEY FOUND" if key else "APIKEY NOT FOUND PLEASE CHECK .ENV FILE")
        Logger.print("EMAIL PASSWORD FOUND" if mail_password else "EMAIL PASSWORD NOT FOUND PLEASE CHECK .ENV FILE")
        Logger.log("EMAIL PASSWORD FOUND" if mail_password else "EMAIL NOT FOUND PLEASE CHECK .ENV FILE")
        
        if not sender or not key or not mail_password:
            return
        
        Logger.print_interruption()
            
        mail_sender = EmailSender(sender, mail_password)
        getter = NewsGetter(key)
        dbm = DataBaseManager()
        self.users = dbm.load_users()
        
        if not self.users:
            Logger.print("NO USERS FOUND")
            Logger.log("NO USERS FOUND")
            return
        
        Logger.print("NEWSLETTER STARTED")
        Logger.log("NEWSLETTER STARTED")
        Logger.print("SHOWING ALL USERS")
        Logger.log("SHOWING ALL USERS")
        Logger.print(f"USERS FOUND: {len(self.users)}")
        Logger.log(f"USERS FOUND: {len(self.users)}")
        Logger.print_interruption()
        ConsoleController.show_users_table(self.users)
        
        while True:
            current_day = TimeGetter.get_current_day()
            new_users = dbm.load_users()
            
            if not dbm.equal_lists(self.users, new_users):
                self.users = new_users.copy()
                Logger.print("DETECTED EDIT IN USERS")
                Logger.log("DETECTED EDIT IN USERS")
                ConsoleController.show_users_table(self.users)

            Logger.print("SEARCHING FOR USERS")
            Logger.log("SEARCHING FOR USERS")
            for user in self.users:
                if user.hour == TimeGetter.get_current_hour() and user.last_sent != current_day:
                    articles = getter.get_news(user.news_category)
                    Logger.print(f"ARTICLES FOUND FOR {user.email}: {len(articles)}")
                    Logger.log(f"ARTICLES FOUND FOR {user.email}: {len(articles)}")
                    content = ""

                    for index, article in enumerate(articles):
                        content = content + ContentFormatter.get_formatted_content(article, index)

                    email = Email(sender, user.email, f"Daily {user.news_category.value.capitalize()} News", content)
                    if mail_sender.send_email(email):
                        Logger.print(f"SENT EMAIL TO {user.email}")
                        Logger.log(f"SENT EMAIL TO {user.email}")
                        user.last_sent = TimeGetter.get_current_day()
                        dbm.update_user_by_id(user)
                        Logger.print("UPDATED USERS TABLE")
                        Logger.log("UPDATED USERS TABLE")
                        ConsoleController.show_users_table(self.users)
                    else:
                        Logger.print(f"NOT SENT EMAIL TO {user.email}")
                        Logger.log(f"NOT SENT EMAIL TO {user.email}")

            time.sleep(60)