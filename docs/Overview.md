# 🥜 Report - In a nutshell

## Introduction

The idea of the project was to get a model that is able to extract light sources from astronomical pictures.

## Generate astronomical pictures

The first step (alpha version) was to create a program that allow to generate simplistic astronomical pictures with a given light source. To do so, the first step was to generate gaussian sources (stars) and to add them to a picture. Then, the noise was added to the picture.

As the pictures was a bit too simplistic, I decided to add a telescope pupil and some diffraction effects to this image to make the stars look a bit more like the usual astronomical pictures. This part was very quick thanks to my experience on a similar project made in the end of my bachelore.

## Design the model

The second step was to design the model. Here is the part on which I spent the most time. In fact, I was expecting to face similar challenges as in a previous project I made in machine learning. But I was wrong because a a detail that change a lot the problem: a such model must have a variable number of outputs. Indeed, the number of light sources in the picture is not fixed.

As I'm a beginer in machine learning and as there is a lot of different tutorial that are focused on specific problems, I made a lot and a lot of tentatives before realizing that the problem I was facing was a bit to complexe to design a model in 20h (I exceeded this time... just a bit...) by myself without having more experience.

## Search for a tranable detection model

I then decided to search for a trainable detection model. I found a lot of models that were able to detect objects in pictures, but for a while, I didn't find any model that was trainable. I finally found a tutorial that explain how to train a model called yoloV5. It is actually one of the most popular object detection model but I was misleaded by other tutorials that said it was pre-trained and not trainable (I think it was because the tutorial was about a specific version of the model that was not trainable).

## Train the model

The last step was to train the model. I used the tutorial I found to train the model on the generated pictures. I had to change the code a bit to save the data in a format the yoloV5 is able to deal with. Unfortunately, I wasn't able to have revelant results for a reason I still ignore...

## Conclusion

The more I get into the machine learning frameworks, the more I realize how wide the field is (number of possible applications and solution for each of them) and how much a unified and structured ressource that make this world more accessible would be awsome! I'm a bit disapointed to not have been able to get a working model, but I'm still happy to have explored a bit deeper this field.

> *I didn't say my last word...*