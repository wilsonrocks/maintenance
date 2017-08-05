from email.message import EmailMessage
from email.policy import default
import smtplib
import datetime

import peewee
from jinja2 import Template

import sys
sys.path.append('/home/dad/maintenance')
import os
os.chdir('/home/dad/maintenance')
from maintain.models import Job, Room, Category
import secrets

#message = EmailMessage(policy=default)
message = EmailMessage()

with open('/home/dad/maintenance/maintain/templates/email.template') as template_file:
    seven_days_ago = peewee.datetime.date.today() - peewee.datetime.timedelta(days=7)
    template = Template(template_file.read())
    message.set_content(template.render(
        completed=(Job
            .select()
            .where(Job.completed >= seven_days_ago)
            .order_by(Job.room, Job.category)),
        incomplete=Job.select().where(Job.completed==None).order_by(Job.room, Job.category)
        ))

message['From'] = secrets.FROM_ADDR
message['To'] = ["oh.that.wilson@googlemail.com", "shelleybullas@googlemail.com"]
message['Subject'] = "Jobs done this week!"

print(message.as_string())

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(secrets.FROM_ADDR, secrets.PASSWORD)
server.send_message(message)
