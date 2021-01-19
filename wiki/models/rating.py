from django.db import models
from django.contrib.auth.models import User
from .node import Node
from .textchoices import RatingTypes

class Rating(models.Model):

    score = models.SmallIntegerField(null=True)

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


    # Admin panel inlines
    def get_type(obj):
        return obj.get_type_display()

    def get_node_title(self):
        return self.node.title;

    def get_user_username(self):
        return self.user.username;

    # Used by django admin, sets the header title for inlines
    get_type.short_description = 'Type'
    get_node_title.short_description = 'Node'
    get_user_username.short_description = 'User'

