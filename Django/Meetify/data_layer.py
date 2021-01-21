import json
from django.db import models
from django.core import serializers as ser
from django.core.exceptions import ValidationError
from .models import *


def serialize(models):
    return json.loads(ser.serialize("json", models))


def validate(model):
    try:
        model.full_clean()
    except ValidationError as e:
        # TODO - Add error handling
        pass


def create_user(user):
    # u = Users(DisplayName=user['DisplayName'], Password=user['Password'],
    #           Email=user['Email'], META_StartDate=user['META_StartDate'])
    # u.save()
    # return u
    return


def find_user(username):
    # u = Users.objects.get(Email=email)
    # return u
    return
