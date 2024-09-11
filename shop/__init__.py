
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# set a secrete key
app.config["SECRET_KEY"] = "b6ee52d0deaf51e633f1b72e0da2cd4c"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///glofarmersMkt.db"

# Create a database instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

# Import routes after initializing app and db
from shop.admin.routes import*
from shop.farmsProducts.routes import*
