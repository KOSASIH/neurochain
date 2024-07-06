import tensorflow as tf

class NeuralNetwork:
    def __init__(self, input_dim, hidden_dim, output_dim):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim

        self.weights1 = tf.Variable(tf.random.normal([input_dim, hidden_dim]))
        self.bias1 = tf.Variable(tf.random.normal([hidden_dim]))
        self.weights2 = tf.Variable(tf.random.normal([hidden_dim, output_dim]))
        self.bias2 = tf.Variable(tf.random.normal([output_dim]))

    def forward(self, x):
        hidden_layer = tf.nn.relu(tf.matmul(x, self.weights1) + self.bias1)
        output_layer = tf.matmul(hidden_layer, self.weights2) + self.bias2
        return output_layer

    def train(self, x_train, y_train, epochs, batch_size):
        optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
        for epoch in range(epochs):
            for i in range(0, len(x_train), batch_size):
                x_batch = x_train[i:i+batch_size]
                y_batch = y_train[i:i+batch_size]
                with tf.GradientTape() as tape:
                    output = self.forward(x_batch)
                    loss = tf.reduce_mean(tf.square(output - y_batch))
                gradients = tape.gradient(loss, self.weights1, self.bias1, self.weights2, self.bias2)
                optimizer.apply_gradients(zip(gradients, [self.weights1, self.bias1, self.weights2, self.bias2]))

    def evaluate(self, x_test, y_test):
        output = self.forward(x_test)
        accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(output, 1), tf.argmax(y_test, 1)), tf.float32))
        return accuracy

nn = NeuralNetwork(input_dim=784, hidden_dim=256, output_dim=10)
nn.train(x_train, y_train, epochs=10, batch_size=128)
accuracy = nn.evaluate(x_test, y_test)
print("Accuracy:", accuracy)
