from django.db import models
from django.contrib.auth.models import User

class Node(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nodes = models.ManyToManyField("self", through="NodeRelation")

    class Meta:
        db_table = "nodes"

    def __str__(self):
        return self.title
