import unittest


class AssertAll(unittest.TestCase):
    def assert_all(self, response, description, status_code=200, status=200):
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(status, response.json().get("status"))
        self.assertEqual(description, str(response.json().get("description")))

    def status_code(self, response, status_code=200):
        self.assertEqual(status_code, response.status_code)

    def statuscode_status(self, response, status_code=200, status=200):
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(status, response.json().get("status"))

    def statuscode_description(self, response, description, status_code=200):
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(description, response.json().get("description"))

    def statuscode_text(self, response, description, status_code=200):
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(description, response.text)
