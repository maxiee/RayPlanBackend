from django.db import models

# Create your models here.
PROJECT_STATUS = (
    ("Todo", "待开始"), 
    ("Doing", "进行中"),
    ("Finish", "已完成"),
    ("Changed", "已变更")
)

class Project(models.Model):
    """
    任务表示一件要做的事情。是最小粒度的行动，不可拆分。
    """
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=32,
        choices = PROJECT_STATUS
    )
    start = models.DateField(null=True)
    deadline = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

TASK_STATUS = (
    ("Todo", "待开始"), 
    ("Doing", "进行中"),
    ("Finish", "已完成"),
    ("Changed", "已变更")
)

class Task(models.Model):
    """
    任务表示一件要做的事情。是最小粒度的行动，不可拆分。
    """
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=32,
        choices = TASK_STATUS
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
