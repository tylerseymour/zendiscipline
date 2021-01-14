from django.db import models

class NodeRelation(models.Model):
    source = models.ForeignKey("Node", on_delete=models.CASCADE, related_name="source")
    type = models.ForeignKey("RelationshipType", null=True, on_delete=models.SET_NULL)
    related = models.ForeignKey("Node", on_delete=models.CASCADE, related_name="related")

    class Meta:
        db_table = "nodes_relations"

    def __str__(self):
        return self.source.title + " is a " + self.type.title + " for " + self.related.title
