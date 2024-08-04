from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# YOLOv8 모델 로드
model = YOLO("yolov8.pt")

# 이미지 로드
image_path = "your_image.jpg"
image = cv2.imread(image_path)

# YOLOv8을 사용하여 객체 탐지
results = model(image)

# 탐지된 객체의 경계 상자 그리기
annotated_image = results[0].plot()

# 객체의 크기 계산
for result in results[0].boxes:
    x1, y1, x2, y2 = result.xyxy[0]  # 경계 상자의 좌상단(x1, y1)과 우하단(x2, y2) 좌표
    width = x2 - x1  # 경계 상자의 너비
    height = y2 - y1  # 경계 상자의 높이
    print(f"객체 크기: 너비={width}, 높이={height}")

    # 경계 상자와 크기를 이미지에 표시
    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    cv2.putText(image, f"W:{int(width)} H:{int(height)}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# 이미지 출력
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
