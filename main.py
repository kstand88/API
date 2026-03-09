from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/employees2")
def get_employees(name: str):
    return {"message": f"{name}님, 반갑습니다!"}