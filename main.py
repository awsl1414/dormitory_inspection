from uvicorn import run

from backend.api import app

if __name__ == "__main__":
    run(app="main:app", reload=True)
