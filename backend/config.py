import os
from dotenv import load_dotenv


# Main configuration class
class Config(object):

    load_dotenv()

    # Set the base directory for the app
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set the secret key for the app
    SECRET_KEY = os.getenv('SECRET_KEY')

    OAUTHLIB_RELAX_TOKEN_SCOPE = True

    # Set the database URI
    SQLALCHEMY_DATABASE_URI = (
        'sqlite:///' + os.path.join(basedir, 'database.sqlite')
    )
    # Do not track modifications to objects
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECURITY_CONFIRMABLE = True

    JWT_SECRET_KEY = os.getenv('SECRET_KEY')

    GOOGLE_OAUTH_CLIENT_ID = os.getenv('GOOGLE_OAUTH_CLIENT_ID')
    GOOGLE_OAUTH_CLIENT_SECRET = os.getenv('GOOGLE_OAUTH_CLIENT_SECRET')


# Configuration for production environment
class ProductionConfig(Config):
    # Do not display debug messages
    DEBUG = False

    # Set cookie to be inaccessible by client-side JavaScript
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    OAUTHLIB_INSECURE_TRANSPORT = False


# Configuration for debug environment
class DebugConfig(Config):
    # Display debug messages
    DEBUG = True
    PROPAGATE_EXCEPTIONS = True

    OAUTHLIB_INSECURE_TRANSPORT = True

# Dictionary mapping environment names to corresponding configuration classes
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}
