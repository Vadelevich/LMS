from celery import shared_task


@shared_task
def check_update_course(course_pk):
    print(course_pk)