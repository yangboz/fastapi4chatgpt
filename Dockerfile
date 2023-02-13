# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7 
FROM python:stretch 

COPY app /code/app

WORKDIR /code

#aliyun index

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 3000

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "3000"]
