from flask import Flask
from models import db, Company, Dev, Freebie

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db.init_app(app)

# Additional configuration if needed

if __name__ == '__main__':
    app.run(debug=True)

