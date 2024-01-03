import base64
from fastapi import APIRouter, Request
import numpy as np
import cv2
from ..schemas import YoloBody

router = APIRouter()

@router.post("/yolo")
def yolo_prediction(request: Request, body: YoloBody):
    try:
        image_bytes = base64.b64decode(body.image)


        file_bytes = np.fromstring(image_bytes, np.uint8)    
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        results = request.app.state.ml_models["yolo"](image)[0]
        boxes = results.boxes.xywh.tolist()
        
        if results.probs:
            labels = results.probs.top1.tolist()
        else:
            labels = [0 for _ in boxes]
        
        res = list(zip(labels, boxes))

        return res
    
    except Exception as ex:
        return {"detail":  str(ex)}
