from ultralytics import YOLO

# load pretrained YOLO model
model = YOLO("yolov8n.pt")

# train model
model.train(
    data="data/data.yaml",
    epochs=20,
    imgsz=640
)