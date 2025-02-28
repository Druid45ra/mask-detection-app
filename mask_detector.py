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
        if prediction[0][0] > 0.5:
            return {'mask': False}
        else:
            return {'mask': True}

    def detect_mask_in_video(self, video_source=0):
        cap = cv2.VideoCapture(video_source)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            label = self.detect_mask(frame)
            cv2.putText(frame, str(label), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow('Mask Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
