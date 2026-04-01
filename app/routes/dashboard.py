
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.dependencies import get_db, role_required
from app.models import Record

router=APIRouter()

@router.get("/summary")
def summary(db: Session=Depends(get_db), user=Depends(role_required(["ADMIN","ANALYST"]))):
    inc=db.query(func.sum(Record.amount)).filter(Record.type=="INCOME").scalar() or 0
    exp=db.query(func.sum(Record.amount)).filter(Record.type=="EXPENSE").scalar() or 0
    return {"income":inc,"expense":exp,"net":inc-exp}
