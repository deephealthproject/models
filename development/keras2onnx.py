import os
import tensorflow as tf
import tf2onnx
import onnx


def convert2onnx(model_path, savepath="models.onnx", input_size=(1, 256, 256, 3)):
    # Load models
    print("Loading models...")
    model = tf.keras.models.load_model(filepath=model_path, compile=False)
    model.summary()

    # Convert to ONNX
    print("Converting models to onnx...")
    input_spec = (tf.TensorSpec(input_size, dtype=tf.float32),)
    onnx_model, _ = tf2onnx.convert.from_keras(model, input_signature=input_spec)

    # Save ONNX to file
    onnx.save(onnx_model, savepath)
    print("Model saved!")


if __name__ == "__main__":
    MODEL_PATH = os.path.join("models.h5")
    SAVEPATH = "./models.onnx"
    INPUT_SIZE = (1, 256, 256, 3)
    convert2onnx(model_path=MODEL_PATH, savepath=SAVEPATH, input_size=INPUT_SIZE)
