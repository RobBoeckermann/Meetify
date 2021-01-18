import json
from django.db import models
from django.core import serializers as ser
from .models import *


def serialize(models):
    return json.loads(ser.serialize("json", models))


def insert_user(user):
    u = Users(DisplayName=user['DisplayName'], Password=user['Password'],
              Email=user['Email'], META_StartDate=user['META_StartDate'])
    u.save()


def select_user(email):
    u = Users.objects.get(Email=email)
    return u
