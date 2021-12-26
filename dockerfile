FROM python:3.9

ENV TZ=Asia/Shanghai

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN /usr/local/bin/python -m pip install --upgrade pip \
    & pip install -i http://pypi.doubanio.com/simple/ pip -U \
    & pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py","runserver" ,"0.0.0.0:8000"]