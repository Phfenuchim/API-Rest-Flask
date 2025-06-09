class Email: 
    def __init__(self, to_email: str, subject: str, body: str, cc=None, bcc=None):
        self.to_email = to_email
        self.subject = subject
        self.body = body
        self.cc = cc or []
        self.bcc = bcc or []

    def __str__(self):
        return f"Email(subject={self.subject}, body={self.body}, to={self.to_email}, cc={self.cc}, bcc={self.bcc})"