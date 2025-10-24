from fastapi import FastAPI

app = FastAPI()

@app.get("/{url}")
async def root(url: str):
    return {"message": f"Hello {url}"}