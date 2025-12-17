from fastapi import FastAPI
from api.routes.ingest import router as ingest_router

app = FastAPI(title="Netflix Ingestion API")

app.include_router(ingest_router)
