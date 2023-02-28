from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User

data_user_1 = {"email": "12reqw@fsd.ru", "password": "123qwe456"}
data_user_2 = {"email": "oliya2023@test.ru", "password": "123qwe456"}


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User(email='12reqw@fsd.ru')
        self.user.set_password('123qwe456')
        self.user.save()

        response = self.client.post("/users/api/token/", data_user_1)
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTORIZATION=f"Bearer {self.access_token}")
        self.client.force_authenticate(user=data_user_1)


    def test_create_user(self):
        response = self.client.post(path="/users/create_user/", data=data_user_2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        response = self.client.post('/users/create_user/', data_user_2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_data = {
            "email": [
                "пользователь с таким Почта уже существует."
            ]
        }
        self.assertEqual(response.json(), expected_data)

        response = self.client.post("/users/api/token/", data_user_2)
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.client.force_authenticate(user=data_user_2)

    def test_update_user(self):
        self.test_create_user()
        response = self.client.put('/users/update_user/1/', data_user_2)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_detail_user(self):
        self.test_create_user()
        response = self.client.get('/users/detail_user/1/',data_user_2)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response = self.client.get('/users/detail_user/2/', data_user_2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
