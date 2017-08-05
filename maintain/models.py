import peewee
from flask import url_for
import datetime


db = peewee.SqliteDatabase("/home/dad/maintenance/jobs.db")

def jobs_count():
    return Job.select().where(Job.completed == None).count()

class Room(peewee.Model):
    class Meta:
        database = db
    name = peewee.CharField(unique=True)
    
    def __str__(self):
        return self.name

class Category(peewee.Model):
    class Meta:
        database = db

    name = peewee.CharField(unique=True)

    def __str__(self):
        return self.name

class Job(peewee.Model):
    class Meta:
        database = db

    created = peewee.DateField(default=peewee.datetime.date.today())
    completed = peewee.DateField(null=True)
    info = peewee.CharField()
    part_of = peewee.ForeignKeyField('self', related_name = "parts", null=True)
    category = peewee.ForeignKeyField(Category, related_name = "jobs")
    room = peewee.ForeignKeyField(Room, related_name = "jobs")

    def __str__(self):
        return "{} (id={})".format(self.info,self.id)

    def complete(self):
        """
        Helper to complete the current task. Uses the current date for the completion date.
        """
        self.completed = peewee.datetime.date.today()
        self.save()

    def complete_url(self):
        """
        Returns the URL for marking this task as completed.
        """
        return url_for('complete',id=self.id)

    def delete_url(self):
        return url_for('delete',id=self.id)
