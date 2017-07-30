
import peewee
from flask import url_for
import datetime


db = peewee.SqliteDatabase("jobs.db")

class Category(peewee.Model):
    class Meta:
        database = db

    name = peewee.CharField(unique=True)

class Job(peewee.Model):
    class Meta:
        database = db

    created = peewee.DateField(default=datetime.date.today())
    completed = peewee.DateField(null=True)
    info = peewee.CharField()
    part_of = peewee.ForeignKeyField('self', related_name = "parts", null=True)
    category = peewee.ForeignKeyField(Category, related_name = "jobs")

    def __str__(self):
        return f"{self.info} (id={self.id})"

    def complete(self):
        """
        Helper to complete the current task. Uses the current date for the completion date.
        """
        self.completed = datetime.date.today()
        self.save()

    def complete_url(self):
        """
        Returns the URL for marking this task as completed.
        """
        return url_for('complete',id=self.id)

    def time_active(self):
        """ Returns how long the task took/how long it's been active. TO BE IMPLEMENTED"""
        pass

