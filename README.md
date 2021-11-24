# DeepHealth Model Zoo

[Open Neural Network Exchange (ONNX)](http://onnx.ai) is an open standard format for representing machine learning models. [Read more](https://github.com/onnx/onnx)

The DeepHealth Model Zoo is a collection of pre-trained models in the ONNX format, that we have check that they are compatible with the lastest version of the [EDDL library](https://github.com/deephealthproject/eddl).

We have standardized on [Git LFS (Large File Storage)](https://git-lfs.github.com/) to store ONNX model files. To download an ONNX model, navigate to the appropriate Github page and click the `Download` button on the top right.

> **Disclaimer:**
> This document is based on the readme from the [onnx/models](https://github.com/onnx/models) repository.

## Models

#### Vision
* [Image Classification](#image_classification)
* [Object Detection & Image Segmentation](#object_detection)
* [Body, Face & Gesture Analysis](#body_analysis)
* [Image Manipulation](#image_manipulation)

#### Language
* [Machine Comprehension](#machine_comprehension)
* [Machine Translation](#machine_translation)
* [Language Modelling](#language_modelling)

#### Other
* [Visual Question Answering & Dialog](#visual_qna)
* [Speech & Audio Processing](#speech)
* [Other interesting models](#others)



### Image Classification <a name="image_classification"/>
This collection of models take images as input, then classifies the major objects in the images into 1000 object categories such as keyboard, mouse, pencil, and many animals.

#### Domain-based Image Classification <a name="domain_based_image"/>
This subset of models classify images for specific domains and datasets.


### Object Detection & Image Segmentation <a name="object_detection"/>
Object detection models detect the presence of multiple objects in an image and segment out areas of the image where the objects are detected. Semantic segmentation models partition an input image by labeling each pixel into a set of pre-defined categories.


### Body, Face & Gesture Analysis <a name="body_analysis"/>
Face detection models identify and/or recognize human faces and emotions in given images. Body and Gesture Analysis models identify gender and age in given image.


### Image Manipulation <a name="image_manipulation"/>
Image manipulation models use neural networks to transform input images to modified output images. Some popular models in this category involve style transfer or enhancing images by increasing resolution.


### Speech & Audio Processing <a name="speech"/>
This class of models uses audio data to train models that can identify voice, generate music, or even read text out loud.


### Machine Comprehension <a name="machine_comprehension"/>
This subset of natural language processing models that answer questions about a given context paragraph.


### Machine Translation <a name="machine_translation"/>
This class of natural language processing models learns how to translate input text to another language.

  
### Language Modelling <a name="language_modelling"/>
This subset of natural language processing models learns representations of language from large corpuses of text.

  
### Visual Question Answering & Dialog <a name="visual_qna"/>
This subset of natural language processing models uses input images to answer questions about those images.


### Other interesting models <a name="others"/>
There are many interesting deep learning models that do not fit into the categories described above.

  
### Visual Question Answering & Dialog <a name="visual_qna"/>
This subset of natural language processing models uses input images to answer questions about those images.


