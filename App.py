from flask import Flask
from routes import expense_routes
import database

app = Flask(__name__)
database.init_db()

app.register_blueprint(expense_routes)

if __name__ == "__main__":
    app.run(debug=True)
