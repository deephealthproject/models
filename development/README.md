# Development

## Requirements

- Python 3.6+
- Requirements

```bash
pip install -r requirements.txt
```


## Convert model from Keras to ONNX

Edit `keras2onnx.py` script and run:

```
python3 keras2onnx.py
```


## Fix ONNX models

Some ONNX models can't be imported directly into the EDDL, so you need to "standarize" them using [ONNX Simplifier](https://github.com/daquexian/onnx-simplifier).

**Installation:**

```
pip3 install -U pip && pip3 install onnx-simplifier
```

**Resnet18 (One input)**: [link](https://github.com/onnx/models/tree/master/vision/classification/resnet)

```
python3 -m onnxsim resnet18-v1-7.onnx resnet18-v1-7_simplify.onnx
```


**MobileNet (One input)**: [link](https://github.com/onnx/models/tree/master/vision/classification/mobilenet)

This models requites the input shape

```
python3 -m onnxsim mobilenetv2-7.onnx mobilenetv2-7_simplified.onnx --input-shape 1,3,224,224
```


**TinyYOLOv3 (Two inputs, one dynamic)**: [link](https://github.com/onnx/models/tree/master/vision/object_detection_segmentation/tiny-yolov3)

This models requires two inputs. You can open the model with electron to check the number of inputs and their expected shapes


```
python3 -m onnxsim tiny-yolov3-11.onnx tiny-yolov3-11_simplified.onnx --dynamic-input-shape --input-shape input_1:1,3,416,416 image_shape:1,2
```

**Note:**

> You need to take into account that not all the layers from all the frameworks are supported. Similarly, quantified models are not supported.
