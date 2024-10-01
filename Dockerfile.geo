# Dockerfile.geo
FROM python:3.10.14-slim

WORKDIR /app

# 필요한 패키지 설치
COPY geo_api.txt ./  
RUN pip install --no-cache-dir -r geo_api.txt

# geo.py 복사
COPY geo_api/geo.py /app/geo.py

# geo.py 실행
CMD ["python", "geo.py"]

# 포트 개방
EXPOSE 5002
