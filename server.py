from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def read_root(request: Request):
    return {"message": "HTTPS server ishlayapti!"}