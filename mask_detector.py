import cv2
import numpy as np
from tensorflow.keras.models import load_model

class MaskDetector:
    def __init__(self, model_path):
        self.model = load_model(model_path)
        self.classes = ['No Mask', 'Mask']

    def preprocess_image(self, image):
        image = cv2.resize(image, (150, 150))  # Resize to match model input
        image = image.astype('float32') / 255.0  # Normalize the image
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        return image

    def detect_mask(self, image):
        processed_image = self.preprocess_image(image)
        prediction = self.model.predict(processed_image)
        if prediction[0][0] > 0.3:
            return {'mask': False}
        else:
            return {'mask': True}
