FROM python:3.8-slim

WORKDIR /usr/src/app

COPY . .

EXPOSE 80

CMD ["python", "./hello_world.py"]

