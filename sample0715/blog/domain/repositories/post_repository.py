from mapper.object_mapper import ObjectMapper

from blog.models import PostData
from blog.domain.entities.post import Post


class PostRepository(object):

    def __init__(self):
        self.mapper = ObjectMapper()
        self.mapper.create_map(Post, PostData)

    def all(self):
        return PostData.objects.all()

    def allOrder(self):
        return PostData.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    def save(self, post):
        post_data = self.mapper.map(post, PostData)
        post_data.save()
