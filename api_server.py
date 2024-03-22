from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import uvicorn
from detector import Detector

app = FastAPI()

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Welcome to WAF Detector!"}


@app.post("/detect/")
async def detect_url(url: str="GET /tienda1/example"):
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")
    else:
        try:
            detector = Detector()
            label_pred = detector.predict_url(url)
            return {"url": url, "label": label_pred}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
        

