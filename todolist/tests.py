from django.test import TestCase
from django.test import TestCase, Client

# Create your tests here.
class ToDoListTest(TestCase):
    def test_todolist_login(self):
        response = Client().get('/todolist/login/')
        self.assertEqual(response.status_code, 200)

    def test_todolist_register(self):
        response = Client().get('/todolist/register/')
        self.assertEqual(response.status_code, 200)

    def test_todolist_create(self):
        response = Client().get('/todolist/create-task/')
        self.assertEqual(response.status_code, 200)