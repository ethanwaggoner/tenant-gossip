from .models import Category, Comment, Post, PostLike, CommentLike


class CategoryService:

    @staticmethod
    def get_all_categories():
        return Category.get_all()

    @staticmethod
    def create_category(name, description):
        return Category.create(name=name, description=description)

    @staticmethod
    def get_category_by_id(category_id):
        return Category.get_by_id(category_id)

    @staticmethod
    def update_category(category, name, description):
        category.update(name=name, description=description)
        return category

    @staticmethod
    def delete_category(category):
        category.delete()
        return {'message': 'Successfully deleted category'}, 200

    @staticmethod
    def get_all_categories_data():
        forums_categories = Category.get_all()
        results = []
        for forums_category in forums_categories:
            category_data = {
                'category_id': forums_category.id,
                'name': forums_category.name,
                'description': forums_category.description,
                'number_of_threads': forums_category.posts.count(),
            }
            results.append(category_data)
        return {'results': results}


class PostService:

    @staticmethod
    def create_post(title, body, category_id, author_id):
        return Post.create(title=title, body=body, category_id=category_id, author_id=author_id)

    @staticmethod
    def get_posts_by_category_id(category_id):
        return Post.get_all_by_category_id(category_id)

    @staticmethod
    def update_post(post, title=None, body=None, category_id=None):
        post.update(title=title, body=body, category_id=category_id)
        return post

    @staticmethod
    def delete_post(post):
        post.delete()
        return {'message': 'Successfully deleted post'}, 200

    @staticmethod
    def get_all_posts_data_by_category_id(category_id):
        all_posts = Post.get_all_by_category_id(category_id)
        results = []
        for post in all_posts:
            post_data = {
                'title': post.title,
                'body': post.body,
                'category_id': post.category_id,
                'author_id': post.author_id,
            }
            results.append(post_data)
        return {'results': results}

    @classmethod
    def get_post_by_id(cls, post_id):
        return Post.get_by_id(post_id)

    @classmethod
    def get_post_by_id_and_category_id(cls, post_id, category_id):
        return Post.get_by_id_and_category_id(post_id, category_id)


class CommentService:

    @staticmethod
    def create_comment(body, post_id, author_id):
        return Comment.create(body=body, post_id=post_id, author_id=author_id)

    @staticmethod
    def get_all_comments():
        return Comment.get_all()

    @staticmethod
    def get_comment_by_post_id_and_comment_id(post_id, comment_id):
        return Comment.get_comment_by_post_id_and_comment_id(post_id, comment_id)

    @staticmethod
    def get_comments_by_post_id(post_id):
        return Comment.get_by_post_id(post_id)

    @staticmethod
    def update_comment(comment, body):
        comment.update(body=body)
        return comment

    @staticmethod
    def delete_comment(comment):
        comment.delete()
        return {'message': 'Successfully deleted comment'}, 200

    @staticmethod
    def get_all_comments_data():
        all_comments = Comment.get_all()
        results = []
        for comment in all_comments:
            comment_data = {
                'body': comment.body,
                'post_id': comment.post_id,
                'author_id': comment.author_id,
            }
            results.append(comment_data)
        return {'results': results}
