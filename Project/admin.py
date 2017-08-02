from django.contrib import admin

from .models import Project, Task, TaskPriority, Category, DailyTask, UserCategory


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(TaskPriority)
class TaskPriorityAdmin(admin.ModelAdmin):
    list_display = ('identifier',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(DailyTask)
class DailyTaskAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(UserCategory)
class UserCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
