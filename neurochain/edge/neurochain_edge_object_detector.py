import tensorflow as tf
from tensorflow import lite

class NeuroChainEdgeObjectDetector:
    def __init__(self):
        self.model = lite.TFLiteModel.from_file('model.tflite')
        self.interpreter = lite.Interpreter(self.model)
        self.interpreter.allocate_tensors()

    def detect(self, image):
        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()
        self.interpreter.set_tensor(input_details[0]['index'], image)
        self.interpreter.invoke()
        output_data = self.interpreter.get_tensor(output_details[0]['index'])
        return output_data

detector = NeuroChainEdgeObjectDetector()
image = load_image('image.jpg')
output = detector.detect(image)
print(output)
