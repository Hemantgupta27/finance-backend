
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db, role_required
from app.models import Record
import datetime

router=APIRouter()

@router.post("/")
def create(data: dict, db: Session=Depends(get_db), user=Depends(role_required(["ADMIN"]))):
    r=Record(amount=data["amount"], type=data["type"], category=data["category"], date=datetime.datetime.utcnow(), user_id=user.id)
    db.add(r); db.commit()
    return r

@router.get("/")
def read(db: Session=Depends(get_db), user=Depends(role_required(["ADMIN","ANALYST","VIEWER"]))):
    return db.query(Record).all()
