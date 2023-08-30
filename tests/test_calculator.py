import unittest
from fastapi.testclient import TestClient
from calculator import app


class TestApp(unittest.TestCase):
    """
    Define a test class that inherits from unittest.TestCase
    The setUp method will be called before executing each test
    Create an instance of TestClient, used for testing FastAPI
    """
    def setUp(self):
        self.client = TestClient(app)

    # Test to check the home page (GET request)
    def test_home(self):
        """
        Test to check the home page (GET request)
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Введите выражение:", response.text)

    def test_calculate_valid(self):
        """
        Test for correctly evaluating an expression (POST request with valid data)
        """
        response = self.client.post("/", data={"expression": "2 + 2"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Результат:", response.text)

    def test_calculate_invalid(self):
        """
        Test for handling the error of division by zero (POST request with invalid data)
        """
        response = self.client.post("/", data={"expression": "2 / 0"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Ошибка:", response.text)


if __name__ == '__main__':
    unittest.main()


# from fastapi.testclient import TestClient
# from calculator import app
#
#
# # Создайте экземпляр TestClient
# client = TestClient(app)
#
#
# def test_home():
#     # Тест для GET запроса на главную страницу
#     response = client.get("/")
#     assert response.status_code == 200
#     assert "Введите выражение:" in response.text
#
#
# def test_calculate_valid():
#     # Тест для POST запроса с корректным выражением
#     response = client.post("/", data={"expression": "2 + 2"})
#     assert response.status_code == 200
#     assert "Результат:" in response.text
#
#
# def test_calculate_invalid():
#     # Тест для POST запроса с некорректным выражением
#     response = client.post("/", data={"expression": "2 / 0"})
#     assert response.status_code == 200
#     assert "Ошибка:" in response.text
