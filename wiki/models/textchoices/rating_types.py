from django.db import models

class RatingTypes(models.TextChoices):

    NONE = 'NIL', 'None'
    EFFECTIVE = 'EFF', 'Effective'
    INEFFECTIVE = 'IEF', 'Ineffective'
    DIFFICULT = 'DIF', 'Difficult'

