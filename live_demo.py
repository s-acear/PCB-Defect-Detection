from ultralytics import YOLO
import cv2

#  Load trained YOLO model (UPDATE PATH IF NEEDED)
model = YOLO("models/pcb_best.pt")

#  DroidCam WiFi stream (REPLACE WITH YOUR IP)
camera_source = "http://YOUR_PHONE_IP:4747/video"  # 

cap = cv2.VideoCapture(camera_source)

if not cap.isOpened():
    print("Error: Could not open camera stream")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to get frame")
        break

    # Run YOLO detection
    results = model.predict(frame, imgsz=320, conf=0.5)

    #  Draw bounding boxes
    annotated_frame = results[0].plot()

    #  Get unique detected defects
    if len(results[0].boxes) == 0:
        text = "No Defect Detected"
        color = (0, 255, 0)  # Green
    else:
        defects = set([results[0].names[int(box.cls)] for box in results[0].boxes])
        text = "Defect: " + ", ".join(defects)
        color = (0, 0, 255)  # Red

    # Resize frame for better display
    annotated_frame = cv2.resize(annotated_frame, (900, 600))

    # Add clean text on screen
    cv2.putText(annotated_frame, text, (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

    # Show window
    cv2.imshow("PCB Defect Detection - Live", annotated_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()