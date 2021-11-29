import argparse
import numpy as np
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.python.data.ops.dataset_ops import AUTOTUNE;


def main() -> None:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]...",
        description="Predict image class using trained model"
    )
    parser.add_argument("file")
    args = parser.parse_args()

    if not args.file:
        print("Please provide a valid image path")
    
    model = tf.keras.models.load_model("./tensorflow_nn/models/saved_models/model_2021_11_22-08_07_30_PM");
    img = tf.keras.utils.load_img(
        args.file,
        target_size=(256,256)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    class_names = ["Healthy", "Unhealthy"]
    print(
        "This image most likely belongs to {} with a {:.2f} percent confidance."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )

if __name__ == "__main__":
    main()