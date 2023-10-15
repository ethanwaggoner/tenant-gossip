from flask_restx import Api

from backend.app.forums import api as forums_api
from backend.app.forums.controllers import ForumsCategoryList


api = Api(
    title='Tenant Gossip API',
    version='1.0',
    description='Tenant Gossip API',
)

api.add_namespace(forums_api)
