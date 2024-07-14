# ベースイメージとしてDebianを使用
FROM debian:latest

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係をインストール
COPY requirements.txt /app/
RUN python3 -m venv venv && . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# ソースコードをコピー
COPY src/ /app/src/

# 環境変数を設定
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# 仮想環境をアクティブにしてメインスクリプトを実行
CMD ["python3", "src/main.py"]
