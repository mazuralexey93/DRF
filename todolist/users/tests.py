from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase

from mainapp.models import Project
from users.models import CustomUser
from users.views import CustomUserViewSet


class TestUserViewSet(TestCase):

    def setUp(self):
        self.admin = get_user_model().objects.create_superuser(
            'admin', 'admin@admin.com', 'admin')
        self.user = get_user_model().objects.create_user(
            'user', 'usermail@mail.om', 'geekbrains')
        self.project = {'name': 'Project222', 'link': 'http://localhost/projects/project/222/'}
        self.project_upd = {'name': 'Project111', 'link': 'http://localhost/projects/project/111/'}

    def test_get_list_guest(self):
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

    def test_get_details_guest(self):
        # 4
        project = Project.objects.create(**self.project)
        client = APIClient()
        response = client.get(f'/api/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_details(self):
        # 5
        project = Project.objects.create(**self.project)
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get(f'/api/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.content)
        client.logout()

    def test_edit(self):
        # 6
        project = Project.objects.create(**self.project)
        client = APIClient()
        client.login(username='admin', password='admin')
        response = client.put(f'/api/projects/{project.id}/',
                              self.project_upd)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=project.id)
        self.assertEqual(project.name, self.project_upd['name'])
        self.assertEqual(project.link, self.project_upd['link'])
        client.logout()
        # print(response.content)
