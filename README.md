# PCB Defect Detection using YOLOv8

A computer vision project that detects and localizes defects in Printed Circuit Boards (PCBs) using YOLOv8 Nano.

## Features
- Detects and localizes six types of PCB defects.
- Uses a trained YOLOv8n object detection model.
- Performs live defect detection through a camera feed.
- Displays bounding boxes and defect labels using OpenCV.

## Defect Classes
1. Mouse Bite
2. Spur
3. Missing Hole
4. Short
5. Open Circuit
6. Spurious Copper

## Technologies Used
- Python
- YOLOv8n (Ultralytics)
- PyTorch
- OpenCV

## Dataset

The project uses a labelled PCB defect dataset containing 10,668 images.

| Split | Images |
|---|---:|
| Training | 8,534 |
| Validation | 1,066 |
| Testing | 1,068 |
| Total | 10,668 |

The dataset is not included in this repository.

## Model Evaluation

Validation results of the trained YOLOv8n model:

| Metric | Score |
|---|---:|
| Precision | 80.29% |
| Recall | 78.34% |
| mAP@0.5 | 81.20% |
| mAP@0.5:0.95 | 37.38% |

These results are from the validation set, not the held-out test set.

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd vision-ai-pcb
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Dataset Setup

Place the PCB dataset in the following structure:

```text
data/
└── pcb-defect-dataset/
    ├── train/
    │   ├── images/
    │   └── labels/
    ├── val/
    │   ├── images/
    │   └── labels/
    └── test/
        ├── images/
        └── labels/
```

## Training

Run:

```bash
python train.py
```

## Live Detection

The trained model is stored at:

`models/pcb_best.pt`

Update the DroidCam camera URL in `live_demo.py` with your own phone's camera stream URL.

Run:

```bash
python live_demo.py
```

Press `q` to exit the live detection window.


