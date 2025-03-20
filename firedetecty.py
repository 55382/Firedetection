import os
from roboflow import Roboflow
from ultralytics import YOLO
from IPython.display import Image

# Roboflow API Key and Project
rf = Roboflow(api_key="#")
project = rf.workspace("-jwzpw").project("continuous_fire")
dataset = project.version(6).download("yolov8")

# Install ultralytics and roboflow locally, if not done
# !pip install ultralytics
# !pip install roboflow

# Train the YOLOv8 model
os.system("yolo task=detect mode=train model=yolov8s.pt data=continuous_fire-6/data.yaml epochs=20 imgsz=640 plots=True")

# View Model Training Charts
Image(filename='runs/detect/train4/results.png', width=600)

# Validate the trained model
os.system("yolo task=detect mode=val model=runs/detect/train2/weights/best.pt data=continuous_fire-6/data.yaml")

# Load the best model and make predictions
model = YOLO("bestfire.pt")
model.predict(source=0, save=True, conf=0.4, show=True)
