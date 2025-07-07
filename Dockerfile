# Dockerfile

FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# requirements 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 모든 파일 복사
COPY . .

# 포트 열고 Django 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
