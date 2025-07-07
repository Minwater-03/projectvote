# Dockerfile

FROM python:3.10-slim

# .pyc 파일 생성 방지 (소스 디렉토리에 불필요한 캐시 파일 생성을 막음)
ENV PYTHONDONTWRITEBYTECODE 1

# 표준 출력 버퍼링 비활성화 (print() 결과가 즉시 출력되도록 함)
ENV PYTHONUNBUFFERED 1


# 작업 디렉토리 설정
WORKDIR /app

# requirements 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 전체 프로젝트 복사
COPY . .

#포트 오픈
EXPOSE 8000

# 포트 열고 Django 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
