from fastapi import FastAPI

from app.routes import users

app = FastAPI()

app.include_router(users.router, prefix='/api')
app.include_router(auth.router, prefix='/api')


@app.get("/")
def read_root():
    return {"message": "Hello World"}
