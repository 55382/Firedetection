# Fire Detection using YOLOv8 and Roboflow

This project utilizes **YOLOv8** for fire detection, integrating **Roboflow** for dataset management and training. The model is trained on a fire detection dataset to identify fire in real-time video streams.

## Features
- **Fire Detection Model**: Uses YOLOv8 for real-time fire detection.
- **Dataset Management**: Downloads and manages datasets via Roboflow.
- **Training and Validation**: Trains and validates a YOLOv8 model on the fire dataset.
- **Real-time Inference**: Runs detection on live video feeds.
- **Automated Visualization**: Displays training results and predictions.

## Installation
### Prerequisites
Ensure you have Python 3.8+ installed and install dependencies:
```sh
pip install ultralytics roboflow
```

## Usage
### 1. Clone the repository
```sh
git clone https://github.com/yourusername/fire-detection.git
cd fire-detection
```

### 2. Set up Roboflow API Key
Edit the script to include your **Roboflow API key** in:
```python
rf = Roboflow(api_key="YOUR_ROBOFLOW_API_KEY")
```

### 3. Download Dataset
The dataset is automatically downloaded using Roboflow:
```python
dataset = project.version(6).download("yolov8")
```

### 4. Train the YOLOv8 Model
Run the following command to start training:
```sh
yolo task=detect mode=train model=yolov8s.pt data=continuous_fire-6/data.yaml epochs=20 imgsz=640 plots=True
```

### 5. Validate the Model
After training, validate the model performance:
```sh
yolo task=detect mode=val model=runs/detect/train2/weights/best.pt data=continuous_fire-6/data.yaml
```

### 6. Run Real-Time Detection
Load the trained model and perform real-time fire detection:
```python
model = YOLO("bestfire.pt")
model.predict(source=0, save=True, conf=0.4, show=True)
```

## Results
- Training logs and performance metrics are saved under `runs/detect/train4/results.png`.
- Inference results are saved in the `runs/detect/` directory.

## Configuration
- Modify `epochs` to train for a longer or shorter duration.
- Adjust `conf` (confidence threshold) for better detection accuracy.
- Use a different `source` for real-time detection (video file, webcam, etc.).




