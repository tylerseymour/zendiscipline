from django.db import models
from django.contrib.auth.models import User
from .textchoices import NodeStatuses, NodeTypes


# A node represents a text object in the system.
class Node(models.Model):

    title = models.CharField(max_length=255)

    # Owner of this Node
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    nodes = models.ManyToManyField("self", through="NodeRelation")

    # Node Types (for normalization)
    type = models.CharField(
        max_length=3,
        choices=NodeTypes.choices,
        default=NodeTypes.NONE
    )

    # If this is a copy, this is where it was copied from
    copied_from = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)

    status = models.CharField(
        max_length=10,
        choices=NodeStatuses.choices,
        default=NodeStatuses.NONE
    )

    class Meta:
        db_table = "nodes"

    def __str__(self):
        return self.title

    def get_user_username(self):
        return self.user.username

    # Used by django admin, sets the header title for inlines
    get_user_username.short_description = 'Username'