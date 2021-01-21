from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Node, NodeRelation, RelationshipType, Comment, Rating


# This following two classes enable inline editing of comments for a node in the django admin user interface
# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#inlinemodeladmin-objects
class CommentInline(admin.TabularInline):
    model = Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_user_username')

class RatingInline(admin.TabularInline):
    model = Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ('get_type', 'score', 'get_node_title', 'get_user_username')

class NodeInline(admin.TabularInline):
    model = Node.nodes.through
    fk_name = "source"
    sortable_by = "title"

class NodeAdmin(SummernoteModelAdmin):
    inlines = [
        CommentInline,
        NodeInline,
        RatingInline
    ]
    list_display = ('title', 'type', 'status', 'get_user_username')
    summernote_fields = 'body'

    class Media:
        js = (
           # "//unpkg.com/@popperjs/core@2" ,
            "admin/popper.js",
            "admin/js/admin/jquery.3.5.1.min.js",
            "admin/jquery-ui/jquery-ui.js",
            "admin/bootstrap/js/bootstrap.js",
            "admin/bootstrap/js/bootstrap.bundle.js",
        )

        css = {
            "all": (
                "admin/bootstrap/css/bootstrap.css",
                "admin/jquery-ui/jquery-ui.css",
                "admin/jquery-ui/jquery-ui.theme.css",
            )
        }


# Docs don't explain, but you need to register the ModelAdmin when registering the base model
admin.site.register(Node, NodeAdmin)
admin.site.register(NodeRelation)
admin.site.register(RelationshipType)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Rating, RatingAdmin)
