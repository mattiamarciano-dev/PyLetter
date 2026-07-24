class Email:
    sender: str
    receiver: str
    subject: str
    body: str

    def __init__(self, sender: str, receiver: str, subject: str, body: str):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
