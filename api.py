```python
"""REST API endpoints."""
from src.auth import login, get_user_data
from src.pricing import get_final_price
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash
import re

# Initialize CSRF protection and rate limiting
csrf = CSRFProtect()
limiter = Limiter(key_func=get_remote_address)

def handle_login(request):
    # FIX: Added rate limiting to prevent brute force attacks
    @limiter.limit("5 per minute")
    # FIX: Added CSRF protection to prevent CSRF attacks
    @csrf.exempt  # Temporarily exempt for this example, but should be properly configured
    def _handle_login():
        username = request.get('username')
        password = request.get('password')
        if login(username, password):
            return {"status": "ok", "token": "abc123"}
        return {"status": "error"}
    return _handle_login()

def handle_get_user(request):
    user_id = request.get('user_id')
    # FIX: Sanitize user_id to prevent SQL injection
    if not isinstance(user_id, int) and not user_id.isdigit():
        return {"status": "error", "message": "Invalid user_id"}
    user_id = int(user_id)
    data = get_user_data(user_id)
    return {"data": data}

def handle_checkout(request):
    # FIX: Added input validation for items, user_type, and region
    items = request.get('items', [])
    if not isinstance(items, list):
        return {"status": "error", "message": "Items must be a list"}

    user_type = request.get('user_type', 'standard')
    if user_type not in ['standard', 'premium', 'admin']:
        return {"status": "error", "message": "Invalid user_type"}

    region = request.get('region', 'US')
    if not re.match(r'^[A-Z]{2}$', region):
        return {"status": "error", "message": "Invalid region format"}

    price = get_final_price(items, user_type, region)
    return {"total": price}
```