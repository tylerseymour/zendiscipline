from django.db import models

class RelationshipType(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        db_table = "relationship_types"

    def __str__(self):
        return self.title
