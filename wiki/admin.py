from django.contrib import admin
from .models import Node, NodeRelation, RelationshipType

admin.site.register(Node)
admin.site.register(NodeRelation)
admin.site.register(RelationshipType)
