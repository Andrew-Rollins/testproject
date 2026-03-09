"""REST API endpoints."""
from src.auth import login, get_user_data
from src.pricing import get_final_price

def handle_login(request):
    # No rate limiting, no CSRF protection
    username = request.get('username')
    password = request.get('password')
    if login(username, password):
        return {"status": "ok", "token": "abc123"}
    return {"status": "error"}

def handle_get_user(request):
    user_id = request.get('user_id')
    # Passes raw user input directly to DB query
    data = get_user_data(user_id)
    return {"data": data}

def handle_checkout(request):
    items = request.get('items', [])
    user_type = request.get('user_type', 'standard')
    region = request.get('region', 'US')
    price = get_final_price(items, user_type, region)
    return {"total": price}
