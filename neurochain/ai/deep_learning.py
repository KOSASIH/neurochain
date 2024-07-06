import tensorflow as tf

class DeepLearningModel:
    def __init__(self):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
        ])
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train, epochs=10)

dl_model = DeepLearningModel()
