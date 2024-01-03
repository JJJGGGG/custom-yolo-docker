from fastapi import FastAPI
from contextlib import asynccontextmanager
from ultralytics import YOLO
import torch
from app.routers import inference

@asynccontextmanager
async def lifespan(app: FastAPI):

    app.state.ml_models = {}

    if torch.cuda.is_available():
       device = "cuda"
    else:
       device = "cpu"

    # Load the yolo model
    yolo = YOLO("./sam_images/custom_yolo_model.pt").to(device)

    app.state.ml_models["yolo"] = yolo
    yield

    # Clean up the ML models and release the resources
    app.state.ml_models.clear()

app = FastAPI(lifespan=lifespan)

app.include_router(inference.router)

@app.get("/healthcheck")
def check_working():
    return {"online": True}
