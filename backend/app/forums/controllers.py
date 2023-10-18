from flask_restx import Resource, fields, abort
from . import api
from .services import CategoryService, CommentService, PostService

forums_category_list_model = api.model('forums_category_list_model', {
    'category_id': fields.Integer(required=True, description='ID of the forums category'),
    'name': fields.String(required=True, description='Name of the forums category'),
    'description': fields.String(required=True, description='Description of the forums category'),
    'number_of_threads': fields.Integer(required=True, description='Number of threads in the forums category'),
})

forums_category_list_response_model = api.model('forums_category_response_model',
                                                {'results': fields.List(fields.Nested(forums_category_list_model))})

forums_category_model = api.model('forums_category_model', {
    'name': fields.String(required=True, description='Name of the forums category'),
    'description': fields.String(required=True, description='Description of the forums category'),
})

forums_post_model = api.model('forums_post_model', {
    'title': fields.String(required=True, description='Title of the post'),
    'body': fields.String(required=True, description='Body of the post'),
    'category_id': fields.Integer(required=True, description='ID of the category the post belongs to'),
    'author_id': fields.Integer(required=True, description='ID of the author of the post'),
})

forums_comment_model = api.model('forums_comment_model', {
    'body': fields.String(required=True, description='Body of the comment'),
    'post_id': fields.Integer(required=True, description='ID of the post the comment belongs to'),
    'author_id': fields.Integer(required=True, description='ID of the author of the comment'),
})


@api.route('/categories')
@api.response(404, 'Categories not found')
class ForumsCategoryList(Resource):

    @api.marshal_with(forums_category_list_response_model, code=200)
    @api.response(400, 'Bad request')
    @api.response(401, 'Unauthorized')
    def get(self):
        return CategoryService.get_all_categories_data()

    @api.expect(forums_category_model)
    @api.marshal_with(forums_category_model, code=201)
    def post(self):
        data = api.payload
        forums_category = CategoryService.create_category(name=data.get('name'), description=data.get('description'))
        return forums_category


@api.route('/categories/<int:category_id>')
@api.response(404, 'Category not found')
class ForumsCategory(Resource):

    @api.marshal_with(forums_category_model, code=200)
    @api.response(400, 'Bad request')
    @api.response(401, 'Unauthorized')
    def get(self, category_id: int):
        forums_category = CategoryService.get_category_by_id(category_id)
        if not forums_category:
            abort(404)
        return forums_category

    @api.expect(forums_category_model)
    @api.marshal_with(forums_category_model, code=200)
    def put(self, category_id: int):
        forums_category = CategoryService.get_category_by_id(category_id)
        if not forums_category:
            abort(404)
        data = api.payload
        updated_category = CategoryService.update_category(
            forums_category,
            name=data.get('name', forums_category.name),
            description=data.get('description', forums_category.description)
        )
        return updated_category

    @api.response(200, 'Successfully deleted category')
    def delete(self, category_id: int):
        forums_category = CategoryService.get_category_by_id(category_id)
        if not forums_category:
            abort(404)
        response = CategoryService.delete_category(forums_category)
        return response


@api.route('/categories/<int:category_id>/posts')
class ForumsPostList(Resource):

    @api.marshal_with(forums_post_model, code=200, as_list=True)
    def get(self, category_id: int):
        category = CategoryService.get_category_by_id(category_id)
        if not category:
            abort(404, 'Category not found')
        return PostService.get_posts_by_category_id(category_id)

    @api.expect(forums_post_model)
    @api.marshal_with(forums_post_model, code=201)
    def post(self, category_id: int):
        category = CategoryService.get_category_by_id(category_id)
        if not category:
            abort(404, 'Category not found')
        data = api.payload
        post = PostService.create_post(
            title=data.get('title'),
            body=data.get('body'),
            category_id=category_id,
            author_id=data.get('author_id')
        )
        return post


@api.route('/categories/<int:category_id>/posts/<int:post_id>')
class ForumsPost(Resource):

    @api.marshal_with(forums_post_model, code=200)
    @api.response(404, 'Post not found')
    def get(self, category_id: int, post_id: int):
        post = PostService.get_post_by_id_and_category_id(post_id, category_id)
        if not post:
            abort(404, 'Post not found in the specified category')
        return post

    @api.expect(forums_post_model)
    @api.marshal_with(forums_post_model, code=200)
    def put(self, category_id: int, post_id: int):
        post = PostService.get_post_by_id_and_category_id(post_id, category_id)
        if not post:
            abort(404, 'Post not found in the specified category')
        data = api.payload
        updated_post = PostService.update_post(
            post,
            title=data.get('title', post.title),
            body=data.get('body', post.body)
        )
        return updated_post

    @api.response(200, 'Successfully deleted post')
    def delete(self, category_id: int, post_id: int):
        post = PostService.get_post_by_id_and_category_id(post_id, category_id)
        if not post:
            abort(404, 'Post not found in the specified category')
        response = PostService.delete_post(post)
        return response


@api.route('/categories/<int:category_id>/posts/<int:post_id>/comments')
class ForumsCommentList(Resource):

    @api.marshal_with(forums_comment_model, code=200, as_list=True)
    def get(self, category_id: int, post_id: int):
        post = PostService.get_post_by_id(post_id)
        if not post or post.category_id != category_id:
            abort(404, 'Post not found in the specified category')
        return CommentService.get_comments_by_post_id(post_id)

    @api.expect(forums_comment_model)
    @api.marshal_with(forums_comment_model, code=201)
    def post(self, category_id: int, post_id: int):
        post = PostService.get_post_by_id(post_id)
        if not post or post.category_id != category_id:
            abort(404, 'Post not found in the specified category')
        data = api.payload
        comment = CommentService.create_comment(
            body=data.get('body'),
            post_id=post_id,
            author_id=data.get('author_id')
        )
        return comment


@api.route('/categories/<int:category_id>/posts/<int:post_id>/comments/<int:comment_id>')
class ForumsComment(Resource):

    @api.marshal_with(forums_comment_model, code=200)
    @api.response(404, 'Comment not found')
    def get(self, category_id: int, post_id: int, comment_id: int):
        comment = CommentService.get_comment_by_post_id_and_comment_id(post_id, comment_id)
        if not comment:
            abort(404, 'Comment not found in the specified post')
        return comment

    @api.expect(forums_comment_model)
    @api.marshal_with(forums_comment_model, code=200)
    def put(self, category_id: int, post_id: int, comment_id: int):
        comment = CommentService.get_comment_by_post_id_and_comment_id(post_id, comment_id)
        if not comment:
            abort(404, 'Comment not found in the specified post')
        data = api.payload
        updated_comment = CommentService.update_comment(
            comment,
            body=data.get('body', comment.body)
        )
        return updated_comment

    @api.response(200, 'Successfully deleted comment')
    def delete(self, category_id: int, post_id: int, comment_id: int):
        comment = CommentService.get_comment_by_post_id_and_comment_id(post_id, comment_id)
        if not comment:
            abort(404, 'Comment not found in the specified post')
        response = CommentService.delete_comment(comment)
        return response


api.add_resource(ForumsCategoryList, endpoint='forum')
api.add_resource(ForumsCategory, endpoint='forum/<int:category_id>')
api.add_resource(ForumsPostList, endpoint='forum/<int:category_id>/posts')
api.add_resource(ForumsPost, endpoint='forum/<int:category_id>/posts/<int:post_id>')
api.add_resource(ForumsCommentList, endpoint='forum/<int:category_id>/posts/<int:post_id>/comments')
api.add_resource(ForumsComment, endpoint='forum/<int:category_id>/posts/<int:post_id>/comments/<int:comment_id>')


