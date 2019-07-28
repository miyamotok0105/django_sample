
from blog.domain.repositories.post_repository import PostRepository

class PostService(object):
    def __init__(self):
        self.post_repository = PostRepository()

    def all(self):
        post = self.post_repository
        return post.all()
