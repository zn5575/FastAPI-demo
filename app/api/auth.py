from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import crud, schemas
from app.dependencies import get_db

router = APIRouter()


@router.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: schemas.AuthForm, db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = crud.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me", response_model=schemas.User)
def read_users_me(current_user: schemas.User = Depends(crud.get_current_user)):
    return current_user


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@router.post("/login/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user is None:
        user = crud.create_user(db=db, user=user)
    access_token = crud.create_access_token(data={"sub": user.username})
    return {
        "success": "true",
        "data": {
            "username": user.username,
            "roles": ["admin"],
            "accessToken": access_token,
            # "refreshToken": access_token + ".adminRefresh",
            # "expires": "2023/10/30 00:00:00"
        }
    }
