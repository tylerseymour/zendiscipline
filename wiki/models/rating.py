from django.db import models
from django.contrib.auth.models import User
from .node import Node
from .textchoices import RatingTypes

class Rating(models.Model):

    score = models.SmallIntegerField

    type = models.CharField(
        max_length=3,
        choices=RatingTypes.choices,
        default=RatingTypes.NONE
    )

    # User who made the comment
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Node the comment was made on
    node = models.ForeignKey(Node, on_delete=models.CASCADE)

    class Meta:
        db_table = "ratings"

    def __str__(self):
        return self.type




