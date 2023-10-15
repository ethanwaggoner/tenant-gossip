from flask_migrate import Migrate

from backend import create_app
from backend.app.database import db

app = create_app()
Migrate(app, db)

if __name__ == "__main__":
    app.run(port=5001)
