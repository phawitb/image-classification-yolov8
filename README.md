# image-classification-yolov8  
```
data_hand
│   README.md
│   file001.txt    
│
└───train
│   └───class1
│       │   a1.png
│       │   b1.png
│       │   ...
│   └───class2
│       │   a1.png
│       │   b1.png
│       │   ...
└───test
└───valid
```
    
# train
yolo task=classify mode=train model=yolov8n-cls.pt data=C:\Users\phawit\Documents\image-classification\data_hand epochs=1000 imgsz=128 batch=2
yolo task=classify mode=train model=yolov8n-cls.pt data=C:\Users\phawit\Documents\image-classification\data_animal epochs=1000 imgsz=128 batch=1

# test
yolo task=classify mode=predict model=C:\Users\phawit\Documents\image-classification\runs\classify\train\weights\best.pt conf=0.25 source=C:\Users\phawit\Documents\image-classification\data\test\1  
  
ai_predict.py  
