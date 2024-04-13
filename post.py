import requests


class Post:
    def __init__(self, ):
        self.response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

    def blog_title(self, blog_id):
        return self.response[blog_id]["title"]

    def blog_subtitle(self, blog_id):
        return self.response[blog_id]["subtitle"]

    def blog_body(self, blog_id):
        return self.response[blog_id]["body"]
