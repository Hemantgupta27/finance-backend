
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import User
from app.auth import hash_password, verify_password, create_token

router=APIRouter()

def get_db():
    db=SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/register")
def register(data: dict, db: Session = Depends(get_db)):
    user = User(
        email=data["email"],
        password=hash_password(data["password"]),
        role=data["role"]
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "id": user.id,
        "email": user.email,
        "role": user.role.value
    }

@router.post("/login")
def login(data: dict, db: Session=Depends(get_db)):
    user=db.query(User).filter(User.email==data["email"]).first()
    if not user or not verify_password(data["password"], user.password):
        return {"error":"invalid"}
    return {"token":create_token({"email":user.email,"role":user.role.value})}
