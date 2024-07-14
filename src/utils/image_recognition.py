import cv2

def recognize_image(image_path):
    # 画像を読み込む
    image = cv2.imread(image_path)
    # 画像処理を行う（仮の処理）
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return f"Processed image size: {gray_image.shape}"
