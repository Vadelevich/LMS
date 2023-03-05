import requests
from django.conf import settings
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.test import APITestCase
from rest_framework import status

from training.models import Course
from users.models import User, Payment


class CourseTestCaseUser(APITestCase):
    def setUp(self) -> None:
        self.user = User(email="foo@bar.com")
        self.user.set_password("some_password")
        self.user.save()

        response = self.client.post("/users/api/token/", {"email": "foo@bar.com", "password": "some_password"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        response = self.client.post("/training/create_course/", {"title": "test"})

        self.course = Course.objects.get(title="test")

    def test_course_create(self):
        response = self.client.post("/training/create_course/", {"title": "test"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_data = {
            "title": "test",
            "image": None,
            "description": None
        }
        self.assertEqual(response.json(), expected_data)

    def test_course_list(self):
        response = self.client.get("/training/list_course/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = [{
            "title": "test",
            "image": None,
            "description": None
        }]
        self.assertEqual(response.json(), expected_data)

    def test_course_update(self):
        response = self.client.put(f'/training/update_course/{self.course.id}/', {"title": "test1"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {'title': 'test1', 'image': None, 'description': None}
        self.assertEqual(response.json(), expected_data)

    def test_course_detail(self):
        response = self.client.get(f"/training/retrieve_course/{self.course.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            "title": "test",
            "image": None,
            "description": None,
            'lesson_count': 0,
            'lesson': []
        }
        self.assertEqual(response.json(), expected_data)

    def test_course_destroy(self):
        response = self.client.delete(f"/training/destroy_course/{self.course.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User(email="foo@bar.com")
        self.user.set_password("some_password")
        self.user.save()

        response = self.client.post("/users/api/token/", {"email": "foo@bar.com", "password": "some_password"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTORIZATION=f"Bearer {self.access_token}")

    def test_lesson_create(self):
        response = self.client.post("/training/create_lesson/", {
            "title": "new",
            "link_video": "https: // www.youtube.com"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_data = {'title': 'new', 'image': None, 'description': None, "link_video": "https: // www.youtube.com"}
        self.assertEqual(response.json(), expected_data)

    def test_lesson_update(self):
        self.test_lesson_create()
        response = self.client.put("/training/update_lesson/1/", {
            "title": "new",
            "link_video": "https: // www.youtube.com"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {"title": "new", "image": None, "description": None, "link_video": "https: // www.youtube.com"}
        self.assertEqual(response.json(), expected_data)

    def test_lesson_list(self):
        self.test_lesson_create()
        response = self.client.get('/training/list_lesson/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = [
            {"title": "new", "image": None, "description": None, "link_video": "https: // www.youtube.com"}]
        self.assertEqual(response.json(), expected_data)

    def test_lesson_delete(self):
        self.test_lesson_create()
        response = self.client.delete('/training/destroy_lesson/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_lesson_detail(self):
        self.test_lesson_create()
        response = self.client.get('/training/retrieve_lesson/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {"title": "new", "image": None, "description": None, "link_video": "https: // www.youtube.com"}
        self.assertEqual(response.json(), expected_data)


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.user = User(email="foo@bar.com")
        self.user.set_password("some_password")
        self.user.save()

        response = self.client.post("/users/api/token/", {"email": "foo@bar.com", "password": "some_password"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTORIZATION=f"Bearer {self.access_token}")

        response = self.client.post("/training/create_course/", {"title": "test"})

    def test_subscription_create(self):
        response = self.client.post("/training/create_subscr/", {"course_id": 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_data = {
            "id": 1,
            "status": "active",
            "course_id": 1
        }
        self.assertEqual(response.json(), expected_data)

    def test_subscription_delete(self):
        response = self.client.put("/training/delete_subscr/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            "id": 1,
            "status": "inactive",
            "course_id": 1
        }
        self.assertEqual(response.json(), expected_data)

