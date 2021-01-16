from django.db import models

class NodeStatuses(models.TextChoices):
    NONE = '', ''
    DONE = 'DONE', 'Done'
    CANCELED = 'CANCELED', 'Canceled'
    WAITING = 'WAITING', 'Waiting'

    IDEA = 'IDEA', 'Idea'
