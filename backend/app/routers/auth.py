import uuid
from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List
from app.models.schemas import UserAuthRequest, UserProfile
from app.core.database import db_store

router = APIRouter(prefix="/auth", tags=["User Authentication & Roles"])

ROLE_LEVELS = {
    "Admin": 1,
    "Manager": 2,
    "Lead Developer": 3,
    "Developer": 4,
    "Junior Developer": 5
}

@router.post("/register")
def register_user(req: UserAuthRequest) -> Dict[str, Any]:
    """Registers a new user with role and reporting assignment."""
    data = db_store.read_all()
    users = data.get("users", [])
    
    # Check if email exists
    for u in users:
        if u["email"].lower() == req.email.lower():
            raise HTTPException(status_code=400, detail="User with this email already exists.")
            
    role = req.role if req.role in ROLE_LEVELS else "Developer"
    
    new_user = {
        "id": f"usr-{uuid.uuid4().hex[:8]}",
        "name": req.name or req.email.split("@")[0].capitalize(),
        "email": req.email,
        "password": req.password,  # In production, use bcrypt hash
        "role": role,
        "hierarchy_level": ROLE_LEVELS.get(role, 4),
        "reports_to": req.reports_to,
        "avatar": f"https://api.dicebear.com/7.x/avataaars/svg?seed={req.name or req.email}",
        "status": "active"
    }
    
    users.append(new_user)
    data["users"] = users
    db_store.write_all(data)
    
    # Remove password from response
    user_resp = {k: v for k, v in new_user.items() if k != "password"}
    return {
        "status": "success",
        "message": "User registered successfully.",
        "user": user_resp,
        "token": f"token-{user_resp['id']}"
    }

@router.post("/login")
def login_user(req: UserAuthRequest) -> Dict[str, Any]:
    """Authenticates user email & password."""
    data = db_store.read_all()
    users = data.get("users", [])
    
    for u in users:
        if u["email"].lower() == req.email.lower() and u["password"] == req.password:
            user_resp = {k: v for k, v in u.items() if k != "password"}
            return {
                "status": "success",
                "message": "Login successful.",
                "user": user_resp,
                "token": f"token-{u['id']}"
            }
            
    raise HTTPException(status_code=401, detail="Invalid email or password.")

@router.get("/users")
def list_users() -> Dict[str, Any]:
    """Lists all registered team members and their roles."""
    data = db_store.read_all()
    users = data.get("users", [])
    sanitized = [{k: v for k, v in u.items() if k != "password"} for u in users]
    return {"users": sanitized}
