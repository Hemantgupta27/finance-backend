
from fastapi import Depends, HTTPException, Header
from jose import jwt
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import User

SECRET="secret"

def get_db():
    db=SessionLocal()
    try: yield db
    finally: db.close()

def get_user(auth: str = Header(None), db: Session = Depends(get_db)):
    if not auth: raise HTTPException(401,"No token")
    token=auth.split()[1]
    data=jwt.decode(token, SECRET, algorithms=["HS256"])
    user=db.query(User).filter(User.email==data["email"]).first()
    if not user: raise HTTPException(401,"User not found")
    return user

def role_required(roles):
    def wrapper(user=Depends(get_user)):
        if user.role.value not in roles:
            raise HTTPException(403,"Forbidden")
        return user
    return wrapper
