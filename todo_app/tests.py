from django.test import LiveServerTestCase
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from selenium import webdriver

from todo_app.models import Task
from todo_app.serializers import TaskSerializer


class TaskSerializerUnitTest(TestCase):

    def test_serializer(self):
        task_data = {
            'title': 'New task',
            'description': 'This is a test'
        }
        serializer = TaskSerializer(data=task_data)
        self.assertTrue(serializer.is_valid())


class TaskAPITest(APITestCase):

    def setUp(self):
        task_data = {
            'title': 'New task',
            'description': 'This is a test'
        }
        url = '/api/tasks/'
        self.response = self.client.post(url, task_data, format='json')

    def test_get_task_list(self):
        url = '/api/tasks/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        task = Task.objects.get(title='New task')
        self.assertEqual(task.description, 'This is a test')

    def test_patch_task(self):
        task = Task.objects.get(title='New task')
        task_pk = task.pk
        url = f'/api/tasks/{task_pk}/'
        data = {
            'description': 'Content updated'
        }
        response = self.client.patch(url, data, format='json')
        task = Task.objects.get(pk=task_pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(task.title, 'New task')
        self.assertEqual(task.description, 'Content updated')

    def test_put_task(self):
        task = Task.objects.get(title='New task')
        task_pk = task.pk
        url = f'/api/tasks/{task_pk}/'
        data = {
            'title': 'Best Title',
            'description': 'Best Description'
        }
        response = self.client.put(url, data, format='json')
        task = Task.objects.get(pk=task_pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(task.title, 'Best Title')
        self.assertEqual(task.description, 'Best Description')

    def test_delete_task(self):
        task = Task.objects.get(title='New task')
        task_pk = task.pk
        url = f'/api/tasks/{task_pk}/'
        response = self.client.delete(url, format='json')
        task = Task.objects.filter(pk=task_pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(task.count(), 0)


class GeneralFunctionalTests(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_navigate_site(self):
        self.browser.get('http://localhost:8888/api/tasks/')
        assert self.browser.title == 'Task List – Django REST framework'
