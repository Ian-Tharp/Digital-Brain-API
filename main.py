from fastapi import FastAPI

from setup import setup


app = FastAPI()
setup(app)


@app.get("/health")
def health():
    return {"status": "ok"}
