from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/employees")
def get_employees(name):
    return {f"{name}님, 반갑습니다!"}