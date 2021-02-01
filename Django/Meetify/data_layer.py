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
