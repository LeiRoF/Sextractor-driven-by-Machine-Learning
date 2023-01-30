# Getting Started
## 🔌 Setup

This project require:
- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

1. Clone the repository
    ```
    git clone https://github.com/LeiRoF/M2-Sextractor-driven-by-Machine-Learning
    ```

2. Move into the project folder
    ```
    cd M2-Sextractor-driven-by-Machine-Learning
    ```

3. (optional) Create a virtual environment
    ```bash
    python3.10 -m venv venv
    ```
    And activate it:
    ```
    source venv/bin/activate # Linux
    .\venv\Scripts\activate # Windows
    ```

4. Run the setup script
    ```
    python setup.py
    ```

## 🚀 Usage

1. Edit the config file (called `Step_0_Config.py`) as you want.
2. Verify that this config gives you what you expect by opening the `Step_1_Image_verification.ipynb` notebook and running it.
3. Generate a dataset of these images by running the `Step_2_Image_generation.py` program:
    ```
    python Step_2_Image_generation.py
    ```
4. Train the yoloV5 model by running the `Step_3_Train_AI` program:
    ```
    ./Step_3_Train.sh # Linux
    .\Step_3_Train.ps1 # Windows
    ```
    Or alternatively you can run this ugly command (this is the only thing the program above do):
    ```
    cd ./src/yolov5 && python train.py --img 640 --batch 16 --epochs 3 --data "../dataset.yaml" --weights yolov5s.pt
    ```

5. Detect objects in the test set
    ```
    ./Step_4_Detect.sh # Linux
    .\Step_4_Detect.ps1 # Windows
    ```
    Or alternatively you can run this ugly command (this is the only thing the program above do):
    ```
    cd ./src/yolov5 && python detect.py --source "../../data/test/" --weights yolov5s.pt
    ```	