from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase

from users.models import CustomUser
from users.views import CustomUserViewSet


class TestUserViewSet(TestCase):

    def setUp(self):
        self.superuser = get_user_model().objects.create_superuser(
            'admin', 'admin@admin.com', 'admin')
        self.user = get_user_model().objects.create_user(
            'user', 'usermail@mail.om', 'geekbrains')
        self.project = {'name': 'Prject222', 'link': 'http://localhost/projects/project/222/'}

    def test_get_list_not_auth(self):
        # 1
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = CustomUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list(self):
        # 2
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = CustomUserViewSet.as_view({'get': 'list'})
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        """
        !!! 'CustomUserViewSet' object has no attribute 'create'
        Переопределил  def create(self):
        super(CustomUserViewSet, self).create()
        """
        # 3
        data = {'first_name': 'Egor',
                'last_name': 'Sechin',
                'email': 'EES@locla.om'}

        factory = APIRequestFactory()
        request = factory.post('/api/users/', data)
        view = CustomUserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_create_admin(self):
    #     """
    # TypeError: create() takes 0 positional arguments but 2 were given
    # ???
    #     """
    #     data = {'first_name': 'Egor',
    #             'last_name': 'Sechin',
    #             'email': 'EES@locla.om'}
    #
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/users/', data)
    #     view = CustomUserViewSet.as_view({'post': 'create'})
    #     force_authenticate(request, user=self.superuser)
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



