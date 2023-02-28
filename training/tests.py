from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User


class CourseTestCaseUser(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.user = User(email="foo@bar.com")
        password = "some_password"
        self.user.set_password(password)
        self.user.save()

        response = self.client.post("/users/api/token/", {"email": "foo@bar.com", "password": "some_password"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTORIZATION=f"Bearer {self.access_token}")
        self.client.force_authenticate(user=self.user)

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
        self.test_course_create()
        response = self.client.get("/training/list_course/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = [{
            "title": "test",
            "image": None,
            "description": None
        }]
        self.assertEqual(response.json(), expected_data)

    def test_course_update(self):
        self.test_course_create()
        response = self.client.put("/training/update_course/1/", {"title": "test1"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {'title': 'test1', 'image': None, 'description': None}
        self.assertEqual(response.json(), expected_data)

    def test_course_detail(self):
        self.test_course_create()
        response = self.client.get("/training/retrieve_course/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            "title": "test",
            "image": None,
            "description": None
        }
        self.assertEqual(response.json(), expected_data)

    def test_course_destroy(self):
        self.test_course_create()
        response = self.client.delete("/training/destroy_course/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User(email="foo@bar.com")
        password = "some_password"
        self.user.set_password(password)
        self.user.save()

        response = self.client.post("/users/api/token/", {"email": "foo@bar.com", "password": "some_password"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTORIZATION=f"Bearer {self.access_token}")
        self.client.force_authenticate(user=self.user)

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
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        expected_data = {"title":"new","image":None,"description":None,"link_video":"https: // www.youtube.com"}
        self.assertEqual(response.json(),expected_data)

    def test_lesson_list(self):
        self.test_lesson_create()
        response = self.client.get('/training/list_lesson/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = [{"title":"new","image":None,"description":None,"link_video":"https: // www.youtube.com"}]
        self.assertEqual(response.json(),expected_data)

    def test_lesson_delete(self):
        self.test_lesson_create()
        response = self.client.delete('/training/destroy_lesson/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_lesson_detail(self):
        self.test_lesson_create()
        response = self.client.get('/training/retrieve_lesson/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {"title":"new","image":None,"description":None,"link_video":"https: // www.youtube.com"}
        self.assertEqual(response.json(), expected_data)



