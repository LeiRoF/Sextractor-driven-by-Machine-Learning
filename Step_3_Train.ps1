Set-Location -Path ./src/yolov5
python train.py --img 640 --batch 16 --epochs 3 --data "../dataset.yaml" --weights yolov5s.pt
Set-Location -Path ../../