# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7 
FROM python:stretch 

COPY . ./app 

WORKDIR /app
RUN pip install --upgrade pip

RUN pip config set install.trusted-host pypi.tuna.tsinghua.edu.cn
RUN pip3 install -r requirements.txt
EXPOSE 3000

CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "3000"]
