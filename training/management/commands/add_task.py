from django.core.management import BaseCommand
from datetime import datetime, timedelta

from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):

    def handle(self, *args, **options):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.SECONDS, )
        PeriodicTask.objects.create(
            interval=schedule,  # we created this above.
            name='Check status',  # simply describes this periodic task.
            task='training.tasks.check_status',  # name of task.
            # args=json.dumps(['arg1', 'arg2']),
            # kwargs=json.dumps({
            #     'be_careful': True, }),
            expires=datetime.utcnow() + timedelta(seconds=30)
        )
