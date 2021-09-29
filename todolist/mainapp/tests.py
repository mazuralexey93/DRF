from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from mainapp.models import Project


class TestProjectViewSet(APITestCase):

    def setUp(self):
        self.admin = get_user_model().objects.create_superuser(
            'admin', 'admin@admin.com', 'admin')
        self.user = get_user_model().objects.create_user(
            'user', 'usermail@mail.om', 'geekbrains')
        self.project = {'name': 'Project222',
                        'link': 'http://localhost/projects/project/222/'}
        self.project_upd = {'name': 'Project111',
                            'link': 'http://localhost/projects/project/111/'}

    def test_get_list(self):
        # 7
        self.client.login(username='admin', password='admin')
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_edit_admin(self):
        # 8
        project = Project.objects.create(**self.project)
        project.users.set([self.admin, self.user])
        self.client.login(username='admin', password='admin')
        response = self.client.put(f'/api/projects/{project.id}/',
                                   self.project_upd)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()
        print(response.content)
