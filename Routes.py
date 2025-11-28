from flask import Blueprint, request, jsonify
from models import add_expense, get_all_expenses

expense_routes = Blueprint("expense_routes", __name__)

@expense_routes.route("/expenses", methods=["POST"])
def create_expense():
    data = request.get_json()
    add_expense(data["title"], data["amount"], data["category"])
    return jsonify({"message": "Expense added successfully"})

@expense_routes.route("/expenses", methods=["GET"])
def list_expenses():
    expenses = get_all_expenses()
    return jsonify([dict(e) for e in expenses])
