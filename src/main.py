import os
from utils import chatgpt, image_recognition

def main():
    # ChatGPTの応答を取得
    chat_response = chatgpt.get_response("Hello, ChatGPT!")
    print(f"ChatGPT response: {chat_response}")

    # 画像認識の結果を取得
    image_result = image_recognition.recognize_image("path/to/image.jpg")
    print(f"Image recognition result: {image_result}")

if __name__ == "__main__":
    main()
