#도커가 기본적으로 제공하는 '파이썬이 설치된 이미지' 불러오기
FROM python:3.13.3-alpine

# 프로젝트의 작업 폴더를 /usr/src/app으로 지정
WORKDIR /usr/src/app

# 파이썬이 소스코드를 컴파일해서 확장자 .pyc인 파일을 생성하는 것을 막는다. 사유:도커에선 불필요.
ENV PYTHONDONTWRITEBYTECODE 1

# 파이썬 로그가 버퍼링 없이 즉각 출력되게 할 것
ENV PYTHONUNBUFFERED 1

#requirements.txt의 라이브러리 설치를 위해 필요한 라이브러리(gcc, musl-dev등) 미리 설치하기
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

#현 위치(도커파일 위치)의 파일 전부 아까 지정한 '작업폴더'에 복사해넣기. .(dot)이 현재폴더. /sur/src/app이 작업폴더.
COPY . /usr/src/app/

# requirements.txt의 라이브러리들 설치하기
RUN pip install --upgrade pip
RUN pip install -r requirements.txt