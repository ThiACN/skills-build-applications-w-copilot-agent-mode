from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes team')
        dc = Team.objects.create(name='DC', description='DC superheroes team')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel, is_leader=True)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Banner', email='bruce@marvel.com', team=marvel)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc, is_leader=True)
        diana = User.objects.create(name='Diana Prince', email='diana@dc.com', team=dc)
        barry = User.objects.create(name='Barry Allen', email='barry@dc.com', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, type='Running', duration=50, date=timezone.now().date())
        Activity.objects.create(user=diana, type='Yoga', duration=40, date=timezone.now().date())
        Activity.objects.create(user=barry, type='Sprinting', duration=20, date=timezone.now().date())

        # Create Workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for superheroes', suggested_for='All')
        Workout.objects.create(name='Speed Training', description='Speed workout for speedsters', suggested_for='Barry Allen')
        Workout.objects.create(name='Flight Practice', description='Flight workout for flyers', suggested_for='Clark Kent, Diana Prince')

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, points=120)
        Leaderboard.objects.create(team=dc, points=110)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
