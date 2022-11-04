# 4/11/2022
- Continued to watch [object detection AI tutorial on youtubee](https://www.youtube.com/watch?v=yqkISICHH-U)
  - **LIMITATION**: TensorFlow models use a specific resolution (usually squared) and automatically compress/decompress pictures that are not using this resolution. As we are dealing with small objects on very high resolution pictures, a compression car result to a loss of information and thus a loss of accuracy. We then have to chose or design a model with a large image resolution as input (which will implies long training phase)
  - 3 types of output:
    - Boxes: 2 coordinates representing the box in which there is the object (the most popular one)
    - Keypoints: 1 coordinate on the object -> We are more interested in this one
    - Masks: that  define the border of the iobject

# 3/11/2022
- Continued to watch [object detection AI tutorial on youtubee](https://www.youtube.com/watch?v=yqkISICHH-U)
- Found [collection of models based on TensorFlow 2.0](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) with indication of accuracy, speed and output type.
  - Assuming that we are searching for accuracy, not speed
  - "**CenterNet HourGlass104 Keypoints 1024x1024**" model got the higher score on COCO 2017 dataset.

# 2/11/2022

- Cleaned existing code
  - Added comments
  - Optimized generation
  - Object oriented versions
- Added "shot" module to shorten observation generation code
- Started to watch [object detection AI tutorial on youtubee](https://www.youtube.com/watch?v=yqkISICHH-U)
  - **LIMITATION**: trade-off between speed and precision

# Before

- Sky picture generation module
  - Gaussian sources
  - Gaussian noise
  - Variating magnitude according to probability distribution
- Pupil generation module
  - With central obstruction
  - With spider arms
- Generated fake observations