# ベースイメージとしてDebianを使用
FROM debian:latest

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# 作業ディレクトリを設定
WORKDIR /app

# ソースコードをコピー
COPY src/ /app/src/

# 依存関係をインストール
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

# メインスクリプトを実行
CMD ["python3", "src/main.py"]
