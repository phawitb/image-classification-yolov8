import os
from ultralytics import YOLO

def predict_cls(model,file_name):
    r = model(file_name)
    top5_list = r[0].probs.top5
    top5_cls = [r[0].names[x] for x in top5_list]
    return top5_cls

model_hand = YOLO('best_hand.pt')
model_animal = YOLO('best_animal.pt')

#predict animal
img = 'animal7.png'
predict = predict_cls(model_animal,img)
print(f'img:{img} --> predict:{predict[0]} >> top5:{predict}')


#predict hand
img = 'hand6.png'
predict = predict_cls(model_hand,img)
print(f'img:{img} --> predict:{predict[0]} >> top5:{predict}')
