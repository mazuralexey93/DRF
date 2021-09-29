import json

import coreapi
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase, CoreAPIClient
from mainapp.models import Project
from users.models import CustomUser


class TestProjectViewSet(APITestCase):

    # def setUp(self):
    #     self.admin = get_user_model().objects.create_superuser(
    #         'admin', 'admin@admin.com', 'admin')
    #     self.user = get_user_model().objects.create_user(
    #         'user', 'usermail@mail.om', 'geekbrains')
    #     self.project = {'name': 'Project222',
    #                     'link': 'http://localhost/projects/project/222/'}
    #     self.project_upd = {'name': 'Project111',
    #                         'link': 'http://localhost/projects/project/111/'}
    #
    # def test_get_list(self):
    #     # 7
    #     self.client.login(username='admin', password='admin')
    #     response = self.client.get('/api/projects/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.client.logout()
    #
    # def test_edit_admin(self):
    #     # 8
    #     project = Project.objects.create(**self.project)
    #     # print(self.project)
    #     self.client.login(username='admin', password='admin')
    #     response = self.client.put(f'/api/projects/{project.id}/',
    #                                {'name': 'Project111',
    #                                 'link': 'http://localhost/projects/project/111/'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     project = Project.objects.get(id=project.id)
    #     self.assertEqual(project.name, 'Project111')
    #     self.client.logout()
    #     # print(response.content)
    #
    # def test_edit_admin_mixer(self):
    #     # 9
    #     project = mixer.blend(Project, users=[self.admin, self.user])
    #     # print(self.project)
    #     self.client.login(username='admin', password='admin')
    #     response = self.client.patch(f'/api/projects/{project.id}/',
    #                                  {'link': 'http://localhost/projects/project/111/'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     project = Project.objects.get(id=project.id)
    #     self.assertEqual(project.link, 'http://localhost/projects/project/111/')
    #     self.client.logout()
    #     # print(response.content)
    #
    # def test_get_details_mixer(self):
    #     # 10
    #
    #     project = mixer.blend(Project, name='Very important project',
    #                           users__last_name='Snow')
    #     self.client.login(username='admin', password='admin')
    #     response = self.client.get(f'/api/projects/{project.id}/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     response_project = json.loads(response.content)
    #     self.assertEqual(response_project['name'], 'Very important project')
    #     print(response.content)

    def test_live_get_list(self):
        client = coreapi.Client()
        schema = client.get('http://127.0.0.1:8000/schema')
        # print(schema)
        action = ['token-auth', 'create']
        params = {"username": "admin", "password": "admin"}
        result = client.action(schema, action, params, validate=True)
        # print(result)

        auth = coreapi.auth.TokenAuthentication(
            scheme='Token',
            token=result['token']
        )
        client = coreapi.Client(auth=auth)
        schema = client.get('http://127.0.0.1:8000/schema')
        # print(schema)

        action = ['todos', 'list']
        data = client.action(schema, action)
        self.assertEqual(len(data), 4)
        print(data)
