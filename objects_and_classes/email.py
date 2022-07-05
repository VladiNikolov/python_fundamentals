class Email:
    def __init__(self, sender, receiver, content, is_send = False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False


    def send(self):
        self.is_send = True


    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"

emails = []

input_line = input()

while not input_line == "Stop":
    tokens = input_line.split()
    sender = tokens[0]
    receiver = tokens[1]
    content = tokens[2]
    email = Email(sender, receiver, content)
    emails.append(email)

    input_line = input()
send_emails = input().split(", ")
send_emails = [int(i) for i in send_emails]

for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())