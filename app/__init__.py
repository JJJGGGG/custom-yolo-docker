from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
def check_working():
    return {"online": True}
