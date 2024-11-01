from locust import HttpUser, TaskSet, task, between
import random


class UserBehavious(TaskSet):

    @task
    def like_post(self):
        post_id = 1
        self.client.get(f'/post_like/{post_id}/',
                        data = {},
                        headers = {"Content-Type" : "application/json"}
                        )
        
class WebsiteUser(HttpUser):
    tasks = [UserBehavious]
    wait_time = between(1, 2)