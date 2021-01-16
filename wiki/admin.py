from django.contrib import admin
from .models import Node, NodeRelation, RelationshipType, Comment


# This following two classes enable inline editing of comments for a node in the django admin user interface
# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#inlinemodeladmin-objects
class CommentInline(admin.TabularInline):
    model = Comment

class NodeInline(admin.TabularInline):
    model = Node.nodes.through
    fk_name = "source"

class NodeAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        NodeInline
    ]

# Docs don't explain, but you need to register the ModelAdmin when registering the base model
admin.site.register(Node, NodeAdmin)


admin.site.register(NodeRelation)
admin.site.register(RelationshipType)
admin.site.register(Comment)
