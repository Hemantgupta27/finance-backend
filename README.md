# 💰 Finance Backend System 

##  Overview

This project is a backend system for a finance dashboard that manages financial records, user roles, and summary analytics.

The goal of this implementation is not to build a production-ready system, but to demonstrate **clean backend design, logical structuring, and clear engineering thinking**.

---

##  Objectives

* Design a well-structured backend system
* Implement role-based access control (RBAC)
* Manage financial records efficiently
* Provide aggregated data for dashboard insights
* Ensure clarity, maintainability, and correctness

---

##  Tech Stack

* **Backend Framework:** FastAPI
* **Database:** SQLite (SQLAlchemy ORM)
* **Authentication:** JWT (JSON Web Token)
* **API Documentation:** Swagger (auto-generated)
* **Language:** Python

---

##  Project Structure

```
app/
├── routes/        # API endpoints
├── models/        # Database models
├── dependencies/  # Auth & RBAC logic
├── auth.py        # JWT & password handling
├── db.py          # Database setup
└── main.py        # Entry point
```

---

##  Role-Based Access Control

| Role    | Permissions                          |
| ------- | ------------------------------------ |
| Viewer  | View records only                    |
| Analyst | View records + analytics             |
| Admin   | Full access (create, update, delete) |

Access control is enforced using **dependency-based role checks** at the API level.

---

## Features

### 🔹 User Management

* Register and login users
* Assign roles (Admin / Analyst / Viewer)

###  Financial Records

* Create records (Admin only)
* View records (All roles)
* Structured data: amount, type, category

###  Dashboard APIs

* Total income
* Total expenses
* Net balance
* Aggregated responses for efficient frontend usage

---

##  How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open API Docs:

```
http://localhost:8000/docs
```

---

##  API Testing Flow

1. Register user → `/auth/register`
2. Login → `/auth/login` → get token
3. Authorize → Bearer token
4. Create record → `/records`
5. View summary → `/dashboard/summary`

---

## Assumptions

* Only Admin users can create financial records
* JWT is used for stateless authentication
* SQLite is used for simplicity and quick setup
* Input validation is kept minimal for clarity

---

##  Design Decisions

* Chose **FastAPI** for simplicity and built-in API documentation
* Used **SQLite** to reduce setup complexity during evaluation
* Implemented **RBAC using dependency injection** for clean separation
* Designed **aggregated dashboard APIs** to reduce frontend processing
* Focused on **readability and maintainability over complexity**

---

##  Trade-offs

* SQLite instead of scalable DB (for simplicity)
* Minimal validation (focus on structure and logic)
* Limited features to keep implementation clean

---

##  Future Improvements

* Add pagination and filtering
* Implement advanced analytics (monthly trends, category insights)
* Add refresh tokens for better authentication
* Introduce unit and integration tests
* Deploy with PostgreSQL and Docker

---

##  Conclusion

This project focuses on demonstrating **backend engineering fundamentals**, including:

* Clean architecture
* Proper data modeling
* Role-based access control
* Logical API design

The implementation prioritizes **clarity, correctness, and maintainability**, aligning with the goals of the assignment.

---
