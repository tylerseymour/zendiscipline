from django.contrib import admin
from .models import Node, NodeRelation, RelationshipType, Comment, Rating


# This following two classes enable inline editing of comments for a node in the django admin user interface
# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#inlinemodeladmin-objects
class CommentInline(admin.TabularInline):
    model = Comment

class RatingInline(admin.TabularInline):
    model = Rating

class NodeInline(admin.TabularInline):
    model = Node.nodes.through
    fk_name = "source"
    sortable_by = "title"

class NodeAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        NodeInline,
        RatingInline
    ]

# Docs don't explain, but you need to register the ModelAdmin when registering the base model
admin.site.register(Node, NodeAdmin)


admin.site.register(NodeRelation)
admin.site.register(RelationshipType)
admin.site.register(Comment)
admin.site.register(Rating)
