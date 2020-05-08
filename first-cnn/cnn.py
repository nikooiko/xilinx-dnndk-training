# Imports
import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

class Cnn:
    CP_DIR = 'data/checkpoints'
    DEFAULT_CP = 'default_cp'
    CLASS_NAMES = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
                        "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
    def __init__(self, auto_train = True):
        self.check_path(Cnn.CP_DIR) # make sure that checkpoint directories exists
        self.model = self.create_model()
        self.data = None
        loaded = self.load()
        if auto_train and not loaded:
            self.train()
            self.save()

    def create_model(self):
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation=tf.nn.relu),
            keras.layers.Dense(10, activation=tf.nn.softmax)
        ])
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        return model

    def fetch_data(self):
        fashion_mnist = keras.datasets.fashion_mnist
        (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
        # Preprocess
        train_images = train_images / 255.0
        test_images = test_images / 255.0
        return (train_images, train_labels), (test_images, test_labels)
        
    def prepare_data(self):
        if self.data is None:
            self.data = self.fetch_data()

    def train(self):
        self.prepare_data()

        # Training
        (train_images, train_labels), (test_images, test_labels) = self.data
        self.model.fit(train_images, train_labels, epochs = 5)
        loss, acc = self.model.evaluate(test_images,  test_labels, verbose=2)
        print("Test loss='{}', 'accuracy='{}'".format(loss, acc))
        return [loss, acc]
    
    def save(self, cp_name = DEFAULT_CP):
        cp_dir = "{}/{}".format(Cnn.CP_DIR, cp_name)
        self.check_path(cp_dir)
        tf.contrib.saved_model.save_keras_model(self.model, cp_dir)
    
    def load(self, cp_name = DEFAULT_CP):
        cp_dir = "{}/{}".format(Cnn.CP_DIR, cp_name)
        if not os.path.exists(cp_dir):
            print("Cp='{}' not found".format(cp_name))
            return False # no checkpoint, unable to load
        checkpoints = os.listdir(cp_dir)
        if not len(checkpoints):
            print("No models found under cp='{}'".format(cp_dir))
            return False # no models found
        latest_name = max(checkpoints)
        latest_path = "{}/{}".format(cp_dir, latest_name)
        self.model = tf.contrib.saved_model.load_keras_model(latest_path)
        print("Restored model='{}'".format(latest_path))
        return True

    def predict(self, img = None):
        # if not provided image, just pick one from fetched data
        if img is None:
            self.prepare_data() # make sure data are fetched
            img = self.data[1][0][0]
        model = self.model
        # Predict
        predictions = model.predict(np.expand_dims(img, 0))
        prediction = predictions[0]
        predicted_label = Cnn.CLASS_NAMES[np.argmax(prediction)]
        print("Result='{}'".format(predicted_label))
        return prediction
    
    def plot_result(self, img, prediction):
        class_names = Cnn.CLASS_NAMES
        predicted_label = class_names[np.argmax(prediction)]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap=plt.cm.binary)
        plt.xlabel("{}".format(predicted_label))
        plt.show()

    def check_path(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def test_image(self):
        self.prepare_data()
        img = cnn.data[1][0][0]
        prediction = cnn.predict(img)
        cnn.plot_result(img, prediction)

if __name__ == "__main__":
    cnn = Cnn()
    cnn.test_image()