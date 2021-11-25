# DeepHealth Model Zoo

[Open Neural Network Exchange (ONNX)](http://onnx.ai) is an open standard format for representing machine learning models. [Read more](https://github.com/onnx/onnx)

The DeepHealth Model Zoo is a collection of pre-trained models in the ONNX format, that we have check that they are compatible with the lastest version of the [EDDL library](https://github.com/deephealthproject/eddl).

We have standardized on [Git LFS (Large File Storage)](https://git-lfs.github.com/) to store ONNX model files. To download an ONNX model, navigate to the appropriate Github page and click the `Download` button on the top right.

> **Disclaimer:**
> 
> This document is a modified version of [onnx/models](https://github.com/onnx/models) repository.

## Models

#### Vision

* [Image Classification](#image_classification)
* [Object Detection & Image Segmentation](#object_detection)


### Image Classification <a name="image_classification"/>

This collection of models take images as input, then classifies the major objects in the images into 1000 object categories such as keyboard, mouse, pencil, and many animals.

|Model Class |Reference |Description |
|-|-|-|
|<b>[ResNet](https://github.com/onnx/models/tree/master/vision/classification/resnet)</b>|[He et al.](https://arxiv.org/abs/1512.03385)|A CNN model (up to 152 layers). Uses shortcut connections to achieve higher accuracy when classifying images. <br> Top-5 error from paper - ~3.6%|
<hr>


### Object Detection & Image Segmentation <a name="object_detection"/>

Object detection models detect the presence of multiple objects in an image and segment out areas of the image where the objects are detected. Semantic segmentation models partition an input image by labeling each pixel into a set of pre-defined categories.

|Model Class |Reference |Description |
|-|-|-|
<hr>
