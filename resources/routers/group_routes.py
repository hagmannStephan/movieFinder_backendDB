from fastapi import APIRouter, Depends, HTTPException
import resources.schemas as schemas
import resources.services.group_service  as group_service
from resources.services.auth_service import get_current_user
from resources.services.postgresql_service import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/groups",
    tags=["Groups"]
)


@router.post(
    "/",
    response_model=schemas.Group,
    description="Create a new group",
    responses={
        "200": {"description": "Group created"},
        "500": {"description": "Internal server error"}
    }
)
def create_group(group: schemas.GroupCreate, current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        return group_service.create_group(group, current_user, db)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get(
    "/{id}",
    response_model=schemas.GroupQuery,
    description="Get a group with its members, settings, etc.",
    responses={
        "200": {"description": "Group found"},
        "404": {"description": "Group not found"},
        "401": {"description": "User not authorized"},
        "500": {"description": "Internal server error"}
    }
)
def get_group(id: int, current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        return group_service.get_group(id, current_user, db)
    except Exception as e:
        if str(e) == "Group not found":
            raise HTTPException(status_code=404, detail="Group not found")
        elif str(e) == "User not authorized":
            raise HTTPException(status_code=401, detail="User not authorized")
        else:
            print(e)
            raise HTTPException(status_code=500, detail="Internal server error")
        

# --------------------------------------------------------------------------------------------
# TODO: Implement these endpoints
# --------------------------------------------------------------------------------------------
# PATCH     /groups/{id}                Update a group (settings, admin or name)
# POST      /groups/{id}/members        Add a member with friendship code to a group
# DELETE    /groups/{id}/members/{id}   Remove a member from a group (or leave the group)
# DELETE    /groups/{id}                Delete a group
# GET       /groups/{id}/matches        Get matches of a group
# --------------------------------------------------------------------------------------------