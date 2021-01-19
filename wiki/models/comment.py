from django.db import models
from django.contrib.auth.models import User
from .node import Node

class Comment(models.Model):

    title = models.CharField(max_length=255)

    # User who made the comment
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Node the comment was made on
    node = models.ForeignKey(Node, on_delete=models.CASCADE)

    # The comment this was in response to (if any)
    parent = models.ForeignKey("self", null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.title + " by " + self.user.username

    def get_user_username(self):
        return self.user.username

    # Used by django admin, sets the header title for inlines
    get_user_username.short_description = 'Username'



