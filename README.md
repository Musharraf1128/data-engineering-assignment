# Software Engineering Intern Assignment (Backend)

### ~ Musharraf1128 - All rights reserved

End-to-end data engineering implementation using PostgreSQL, Python ETL, FastAPI, Google Sheets, and NeonDB.

---

## 🎥 Demo

▶️ **[Watch full demo video](./demo.mp4)**
_Shows end-to-end data ingestion, ETL normalization, constraint enforcement, and API verification._

> ⚠️ Demo video is ~77 MB. Please allow a moment for GitHub to load the player.

---

## 1. Setup & Try It Locally

### Prerequisites

* Docker
* Python 3.10+
* Git
* PostgreSQL client (`psql`)

### Clone Repository

```bash
git clone https://github.com/Musharraf1128/data-engineering-assignment
cd data-engineering-assignment
```

### Start PostgreSQL (Local)

```bash
docker compose up -d
```

### Create Schema & Seed Data

```bash
docker exec -i local-postgres psql -U admin -d netflix_db < sql/schema.sql
docker exec -i local-postgres psql -U admin -d netflix_db < sql/seed.sql
```

### Run ETL Pipeline

```bash
python etl/run_etl.py
```

This migrates raw Netflix data into the normalized schema.

---

### Run Backend API (Optional)

```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
```

API will be available at:

```
http://localhost:8000
```

---

### Try Cloud Version (No Local Setup)

* **Backend (Railway):**
  [https://data-engineering-assignment-production.up.railway.app](https://data-engineering-assignment-production.up.railway.app)

* **Google Sheet (Auto-ingestion):**
  [https://docs.google.com/spreadsheets/d/1CTom2rlFVNlxlCdaJJ_tEEM2LKHKRxVQqCVWi5u4HiQ](https://docs.google.com/spreadsheets/d/1CTom2rlFVNlxlCdaJJ_tEEM2LKHKRxVQqCVWi5u4HiQ)

Add a row → data is validated and inserted into NeonDB automatically.

---

## 2. Simple Workflow

```
Raw Dataset / Google Sheet
        ↓
Staging Table (raw, no constraints)
        ↓
Python ETL / FastAPI Validation
        ↓
Normalized PostgreSQL Schema
        ↓
SQL Queries, Views, Procedures
```

### What Happens End-to-End

1. Raw Netflix data or Google Sheet row is added
2. Data is validated & normalized
3. Lookup entities resolved (genres, ratings, people, countries)
4. Inserted safely using FK constraints
5. Queries & analytics run on clean relational data

---

## Notes

* ETL and API logic are **idempotent**
* Schema is fully **3NF**
* Designed for **real-world data ingestion**, not just demos

---
