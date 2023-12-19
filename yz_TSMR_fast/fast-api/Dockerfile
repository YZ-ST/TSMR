# 安裝輕量化的python3.10版本
FROM python:3.10-slim-buster


# Keeps Python from generating .pyc files in the container (防止Python在容器中生成.pyc文件)
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging (關閉緩衝以便更輕鬆地記錄容器的日誌)
ENV PYTHONUNBUFFERED=1

# 設定工作目錄
WORKDIR /app

# 將fast-api的所有內容複製一份到/app裡面 (這邊的路徑是依照，context跟根目錄的路徑)
COPY ./fast-api .


# 將 modules 資料夾複製到容器的 /app/modules 目錄 (這邊的路徑是依照，context跟根目錄的路徑)
COPY ./modules /app/modules


# 升級了Python中的pip工具，並且安裝requirements.txt中的套件
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "uvicorn", "main:app","--host","0.0.0.0", "--port", "5002", "--reload"]



# --host: 設定為0.0.0.0，表示主機與其他的容器都可以訪問到這個fastapi應用程式
# --host: 設定為127.0.0.1，表示容器內部才能訪問到這個fastapi應用程式
# https://blog.csdn.net/Dontla/article/details/129584774

# --port : 設定表示為 fastapi 應用程式要監聽的端口為 5001，需要與 docker-compose.yml 中的 ports 一致都要設置5001，這樣主機5000才能直接方問到容器內部的fastapi應用程式)
# --reload: 自動重整


