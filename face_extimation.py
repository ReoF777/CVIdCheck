from fer import FER
import matplotlib.pyplot as plt

test_image_one = plt.imread('test.jpg')

emo_detector = FER(mtcnn=True)
captured_emotion = emo_detector.detect_emotions(test_image_one)
print(captured_emotion)