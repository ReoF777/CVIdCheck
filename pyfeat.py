import cv2
from fer import FER
import time

# FERオブジェクトを作成
emotion_detector = FER(mtcnn=True)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # カメラからフレームが取得できない場合、ループを終了
    if not ret:
        print("カメラから映像を取得できませんでした。")
        break

    # フレームから表情を解析
    emotion, score = emotion_detector.top_emotion(frame)
    
    print(emotion)

    # 'q'キーでループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    time.sleep(3)

# リソースを解放
cap.release()
cv2.destroyAllWindows()
