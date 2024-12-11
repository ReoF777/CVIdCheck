import cv2
from ultralytics import YOLO

# YOLOモデルのロード
model = YOLO('yolo11n.pt')

# OpenCVでカメラの映像を取得
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# フレームサイズを取得
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# カメラのパン・チルトを制御する関数
def control_camera(x_diff, y_diff):
    """
    x_diff, y_diff: 画像中心から検出されたオブジェクトまでの距離
    この関数内でカメラのモータを制御するコードを記述する。
    例: シリアル通信でモータを動かす場合、pyserialを使用。
    """
    if abs(x_diff) > 20:  # 許容範囲を設定
        if x_diff > 0:
            print("Move camera right")
            # カメラを右に動かすコード
        else:
            print("Move camera left")
            # カメラを左に動かすコード
    
    if abs(y_diff) > 20:
        if y_diff > 0:
            print("Move camera down")
            # カメラを下に動かすコード
        else:
            print("Move camera up")
            # カメラを上に動かすコード

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLOでフレームを解析
    results = model(frame)

    # 検出結果から一番近い人を選択
    closest_person = None
    max_area_value = float('inf')

    for box, cls in zip(results[0].boxes, results[0].boxes.cls):
        name = results[0].names[int(cls)]
        if name == "person":  # 検出対象が「人」であることを確認
            x1, y1, x2, y2 = [int(i) for i in box.xyxy[0]]
            bbox_width = x2 - x1
            bbox_height = y2 - y1
            
            obj_center_x = x1 + bbox_width // 2
            obj_center_y = y1 + bbox_height // 2

            area_value = bbox_width * bbox_height

            if area_value > max_area_value:
                max_area_value = area_value
                closest_person = (obj_center_x, obj_center_y)

    # 一番近い人が検出された場合、カメラを調整
    if closest_person:
        image_center_x = frame_width // 2
        image_center_y = frame_height // 2

        # 画像中心と検出された人の中心の差を計算
        x_diff = closest_person[0] - image_center_x
        y_diff = closest_person[1] - image_center_y

        # カメラを調整
        control_camera(x_diff, y_diff)

    # フレームを表示
    cv2.imshow("Camera", frame)

    # 'q' キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# リソースの解放
cap.release()
cv2.destroyAllWindows()
