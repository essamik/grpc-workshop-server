FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip install grpcio
RUN pip install grpcio-tools

CMD ["python3", "employee_server.py"]