
from django.contrib import admin
from .models import Team, User, Activity, Workout, Leaderboard

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "description")

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "email", "team", "is_leader")

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "type", "duration", "date")

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "suggested_for")

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
	list_display = ("id", "team", "points")
