from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI(title="Smart Parking API", version="0.1.0")


class LotIn(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    hourly_rate: float = Field(gt=0, description="Price per started hour")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/lots/{lot_id}")
def get_lot(lot_id: int, details: bool = False) -> dict:
    # lot_id comes from the path, details from the query string (?details=true)
    return {"lot_id": lot_id, "details": details}


@app.post("/lots", status_code=status.HTTP_201_CREATED)
def create_lot(lot: LotIn) -> dict:
    # `lot` is already validated; invalid bodies never reach this line
    return {"message": "created (not saved yet)", "lot": lot.model_dump()}