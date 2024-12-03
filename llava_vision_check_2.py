import ollama, cv2, time

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # cv2.imshow('frame', frame)
    frame = cv2.imencode('.jpg', frame)[1].tostring()
    
    res = ollama.chat(
        model="llava",
        messages=[{
            "role":"user",
            "content":"この画像に写っている人の表情を日本語で答えてください。",
            "images": [frame]
        }]
    )
    
    key = cv2.waitKey(10)
    if key == 27:
        break
    
    time.sleep(1)

cap.release()
cv2.destroyAllWindows() 