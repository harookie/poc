FROM python:3.9.13
LABEL authors="mac"

#pip 업그레이드
COPY requirements.txt .
RUN pip install --upgrade pip
# RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

# 현재 폴더(do_test) 내의 모들 파일들을 이미지에 추가
WORKDIR /root
ADD /src ./src

#EXPOSE 8080

CMD ["python", "/root/src/main.py"]