from django.contrib.syndication.views import Feed

from posts.models import Post


class NewPostsRss(Feed):
    title = "Вастрик.Клуб: Новые посты"
    link = "/posts.rss"
    description = ""
    limit = 20

    def items(self):
        return Post.visible_objects().order_by("-published_at", "-created_at")[:self.limit]

    def item_title(self, item):
        title = item.title
        if item.prefix:
            title = f"{item.prefix} " + title
        if not item.is_public:
            title += " 🔒"
        return title

    def item_description(self, item):
        return item.description