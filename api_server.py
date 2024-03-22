from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import uvicorn
from detector import Detector

app = FastAPI()

class Item(BaseModel):
    method: str="GET"
    uri: str="/tienda1/example"

@app.get("/")
async def read_root():
    return {"message": "Welcome to WAF Detector!"}


@app.post("/detect/")
async def detect_url(item: Item):
    try:
        method = item.method.upper().strip()
        uri = item.uri.strip()
        payload = method + " " + uri
        detector = Detector()
        label_pred = detector.predict_url(payload)
        return {"method": method, "uri": uri, "label": label_pred}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
        

