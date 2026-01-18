from fastapi import FastAPI
from app.caesar import caesar_cipher

app = FastAPI()

@app.post("/transform/caecar")

def caecar_endpoint(plaintext: str, key: int):
    result = caesar_cipher(plaintext, key)
    return {"result": result}