
from fastapi import FastAPI
from app.db import Base, engine
from app.routes import auth, records, dashboard

Base.metadata.create_all(bind=engine)

app=FastAPI(title="Finance Backend")

app.include_router(auth.router, prefix="/auth")
app.include_router(records.router, prefix="/records")
app.include_router(dashboard.router, prefix="/dashboard")
