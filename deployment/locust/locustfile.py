from locust import HttpUser, task, between

class User(HttpUser):
    wait_time = between(0, 0)

    @task
    def index(self):
        self.client.get("/")
    
    @task
    def about_page(self):
         self.client.get("/about")