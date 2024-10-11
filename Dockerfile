FROM python:3.12
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["python", "main.py"]