# 🔌 Setup

This project require:
- [Python 3.10](https://www.python.org/downloads/release/python-3100/) or above
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
    python3 -m venv venv
    ```
    And activate it:
    ```
    source venv/bin/activate # Linux
    venv\Scripts\activate.bat # Windows
    ```

4. Install the requirements
    ```
    pip install -r requirements.txt
    ```

# 🚀 Usage

1. Edit the config file (called `Step_0_Config.py`) as you want.
2. Verify that this config gives you what you expect by opening the `Step_1_Image_verification.ipynb` notebook and running it.
3. Generate a dataset of these images by running the `Step_2_Image_generation.py` program:
    ```
    python3 Step_2_Image_generation.py
    ```
4. Train the yoloV5 model by running the `Step_3_Train_AI` program:
    ```
    python3 Step_3_Train_AI.py
    ```
    Or alternatively you can run this ugly command (this is the only thing the program above do):
    ```
    cd ./src/yolov5 && python train.py --img 640 --batch 16 --epochs 3 --data "../dataset.yaml" --weights yolov5s.pt
    ```