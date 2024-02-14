# Dockerfile

# 베이스 이미지로 파이썬 3.8 사용
FROM python:3.8-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
RUN pip install Flask==2.0
RUN pip install Werkzeug==2.0 

# 현재 디렉토리의 모든 파일을 컨테이너의 작업 디렉토리로 복사
COPY . .

# Flask 서버 실행
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
