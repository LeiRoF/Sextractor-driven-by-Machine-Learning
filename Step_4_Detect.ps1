Set-Location -Path ./src/yolov5
python detect.py --source "../../data/test/" --weights yolov5s.pt
Set-Location -Path ../../