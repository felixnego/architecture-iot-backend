from locust import HttpUser, task, between


class TestUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def hit_route1(self):
        self.client.get("/route1")

    @task
    def hit_route2(self):
        self.client.get("/route2")

    @task
    def hit_route3(self):
        self.client.get("/route3")
