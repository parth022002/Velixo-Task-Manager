from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List
from app.models.schemas import HierarchyAssignRequest
from app.core.database import db_store
from app.routers.auth import ROLE_LEVELS

router = APIRouter(prefix="/hierarchy", tags=["Team & Organizational Hierarchy"])

@router.get("/tree")
def get_hierarchy_tree() -> Dict[str, Any]:
    """Generates organizational hierarchy tree structure for team mapping."""
    data = db_store.read_all()
    users = data.get("users", [])
    
    # Map user id to dict without password
    user_map = {u["id"]: {k: v for k, v in u.items() if k != "password"} for u in users}
    
    # Build tree
    roots = []
    for u_id, u_info in user_map.items():
        u_info["subordinates"] = []
        
    for u_id, u_info in user_map.items():
        parent_id = u_info.get("reports_to")
        if parent_id and parent_id in user_map:
            user_map[parent_id]["subordinates"].append(u_info)
        else:
            roots.append(u_info)
            
    return {
        "total_members": len(users),
        "roles_summary": {
            "Admin": sum(1 for u in users if u["role"] == "Admin"),
            "Manager": sum(1 for u in users if u["role"] == "Manager"),
            "Lead Developer": sum(1 for u in users if u["role"] == "Lead Developer"),
            "Developer": sum(1 for u in users if u["role"] == "Developer"),
            "Junior Developer": sum(1 for u in users if u["role"] == "Junior Developer")
        },
        "tree": roots
    }

@router.post("/assign")
def assign_hierarchy(req: HierarchyAssignRequest) -> Dict[str, Any]:
    """Admin endpoint to update user role and assign reporting manager link."""
    data = db_store.read_all()
    users = data.get("users", [])
    
    found = False
    for u in users:
        if u["id"] == req.user_id:
            if req.new_role in ROLE_LEVELS:
                u["role"] = req.new_role
                u["hierarchy_level"] = ROLE_LEVELS[req.new_role]
            if req.reports_to is not None:
                u["reports_to"] = req.reports_to if req.reports_to != "" else None
            found = True
            break
            
    if not found:
        raise HTTPException(status_code=404, detail="User not found.")
        
    data["users"] = users
    db_store.write_all(data)
    
    return {"status": "success", "message": "User hierarchy and reporting link updated successfully."}
