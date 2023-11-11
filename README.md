# image-classification-yolov8  
data_hand -- train--cls1--a1.png,b1.png,...  
                  --cls2--a2.png,b2.png,...  
          -- test  
          -- valid  

root
+-- dir1
    +--file1
+-- dir2
    +-- file2
    
# train
yolo task=classify mode=train model=yolov8n-cls.pt data=C:\Users\phawit\Documents\image-classification\data_hand epochs=1000 imgsz=128 batch=2
yolo task=classify mode=train model=yolov8n-cls.pt data=C:\Users\phawit\Documents\image-classification\data_animal epochs=1000 imgsz=128 batch=1

# test
yolo task=classify mode=predict model=C:\Users\phawit\Documents\image-classification\runs\classify\train\weights\best.pt conf=0.25 source=C:\Users\phawit\Documents\image-classification\data\test\1

jupyter notebook
