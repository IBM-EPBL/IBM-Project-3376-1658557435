from locust import HttpUser, task, between

class TestUser(HttpUser):
  @task(1)
  def load_test_auth_page(self):
    self.client.get("http://159.122.174.233:30991/auth/")