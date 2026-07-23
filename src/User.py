from Categories import Categories

class User:
    id: str 
    email: str
    hour: int
    news_category: Categories
    last_sent: str | None
        
    def __init__(self,id: str, email: str, hour: int, news_category: Categories = Categories.GENERAL) -> None:
        self.id = id 
        self.email = email
        self.hour = hour
        self.news_category = news_category
        self.last_sent = None