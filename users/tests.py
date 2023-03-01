from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User(email='12reqw@fsd.ru')
        self.user.set_password('123qwe456')
        self.user.save()

        response = self.client.post("/users/api/token/", {"email": "12reqw@fsd.ru", "password": "123qwe456"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTORIZATION=f"Bearer {self.access_token}")


    def test_create_user(self):
        response = self.client.post(path="/users/create_user/", data={"email": "oliya2023@test.ru", "password": "123qwe456"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        response = self.client.post('/users/create_user/',{"email": "oliya2023@test.ru", "password": "123qwe456"} )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_data = {
            "email": [
                "пользователь с таким Почта уже существует."
            ]
        }
        self.assertEqual(response.json(), expected_data)

    def test_user_detail(self):
        response = self.client.get('/users/detail_user/1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_user_update(self):
        response = self.client.patch('/users/update_user/1/',{"email":"test3@com.ru"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)