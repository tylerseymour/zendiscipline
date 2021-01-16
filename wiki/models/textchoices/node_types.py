from django.db import models

class NodeTypes(models.TextChoices):
    NONE = 'NIL', ''
    BLOG = 'BLG', 'Blog'
    POST = 'PST', 'Post'
    BOOTCAMP = 'BTC', 'Bootcamp'

    # Lists
    CHECKLIST = 'CKL', 'Checklist'
    HABIT_LIST = 'HTL', 'Habit List'
    RITUAL_LIST = 'RLL', 'Ritual List'
    LIST_ITEM = 'ITM', 'List Item'

    # Forums
    FORUM = 'FOR', 'Forum'
    # Use "POST" for forum post

    # WIKI
    FORCING_FUNCTION = 'FFF', 'Forcing Function'
    HABIT = 'HBT', 'Habit'
    IMPLEMENTATION_INTENTION = 'III', 'Implementation Intention'
    REFERENCE = 'REF', 'Reference'
    SCHEMA = 'SCM', 'Schema'
    STRATEGY = 'STR', 'Strategy'

    # PLANNING
    BOARD = 'BRD', 'Board'
    CONCERN = 'CON', 'Concern'
    GOAL = 'GOL', 'Goal'
    JOURNAL = 'JRN', 'Journal'
    NOTE = 'NOT', 'Note'
    PRIORITY = 'PRT', 'Priority'
    PROJECT = 'PRJ', 'Project'
    RETROSPECTIVE = 'RTR', 'Retrospective'
    WORKSHEET = 'WKS', 'Worksheet'

