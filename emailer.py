from email.message import EmailMessage
from email.policy import default
import smtplib

from jinja2 import Template

from maintain.models import Job, Room, Category
import secrets

message = EmailMessage(policy=default)

with open('maintain/templates/email.template') as template_file:
    template = Template(template_file.read())
    message.set_content(template.render(
        name="James",
        completed=Job.select().where(Job.completed).order_by(Job.room),
        incomplete=Job.select().where(Job.completed==None).order_by(Job.room, Job.category)
        ))

message['From'] = secrets.FROM_ADDR
message['To'] = ["oh.that.wilson@googlemail.com", "shelleybullas@googlemail.com"]
message['Subject'] = "Jobs done this week!"

print(message.as_string())

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(secrets.FROM_ADDR, secrets.PASSWORD)
server.send_message(message)
