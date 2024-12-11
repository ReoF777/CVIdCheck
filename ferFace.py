import ollama
import cv2
import time

# res = ollama.chat(
#     model='llama3.2-vision',
#     messages=[{
#         'role': 'user',
#         'content': 'What is the emotion expressed by the person in this image? Choose one of the following: anger, happiness, neutral, sadness, surprise.',
#         'images': ['face.jpg']
#     }]
# )

# print(res['message']['content'])

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imwrite('face.jpg', frame)
    res = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': 'What is the emotion expressed by the person in this image?" \
                        "Choose one of the following: anger, happiness, neutral, sadness, surprise."  \
                        "Only provide the emotion, without any explanation.',
            'images': ['face.jpg']
        }]
    )
    print(res['message']['content'])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    time.sleep(1)
    
cap.release()
cv2.destroyAllWindows()