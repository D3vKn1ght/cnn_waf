from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import uvicorn
import random
import logging
from detector import Detector

app = FastAPI()

class Item(BaseModel):
    method: str="GET"
    uri: str="/tienda1/example"

def format_uri(uri):
    space_char = ["%20", "+"]
    random_space = random.choice(space_char)
    uri = uri.replace(" ", random_space)
    return uri
    

@app.get("/")
async def read_root():
    return {"message": "Welcome to WAF Detector!"}


@app.post("/detect/")
async def detect_url(item: Item):
    try:
        method = item.method.upper().strip()
        uri = item.uri.strip()
        uri = format_uri(uri)
        payload = method + " " + uri
        detector = Detector()
        label_pred = detector.predict_url(payload)
        logging.warning(f"method: {method}, uri: {uri}, label: {label_pred}")
        return {"method": method, "uri": uri, "label": label_pred}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
        

