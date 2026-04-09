from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Use PyMongo to drop collections directly (Djongo workaround)
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        for coll in ['leaderboard', 'activities', 'workouts', 'users', 'teams']:
            db[coll].drop()
        client.close()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=tony, type='Running', duration=30, date=date.today())
        Activity.objects.create(user=steve, type='Cycling', duration=45, date=date.today())
        Activity.objects.create(user=bruce, type='Swimming', duration=60, date=date.today())
        Activity.objects.create(user=clark, type='Yoga', duration=20, date=date.today())

        # Create workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
        w2 = Workout.objects.create(name='Flight Training', description='Aerobic workout for flying heroes')
        w1.suggested_for.set([tony, bruce])
        w2.suggested_for.set([steve, clark])

        # Create leaderboard
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=95)
        Leaderboard.objects.create(user=clark, score=85)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
