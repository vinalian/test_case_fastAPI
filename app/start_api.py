from fastapi import FastAPI
from project.app.main_router import router


app = FastAPI()
app.include_router(router=router, prefix="/api/v1", tags=['main'])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8001)
