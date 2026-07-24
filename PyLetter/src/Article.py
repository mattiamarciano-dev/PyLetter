class Article:
    title: str
    author: str
    source: str
    content: str
    url: str
    img_url: str

    def __init__(self, title: str, author: str, source: str, content: str, url: str, img_url: str) -> None:
        self.title = title
        self.author = author
        self.source = source
        self.content = content
        self.url = url
        self.img_url = img_url