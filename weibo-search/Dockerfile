FROM python:3.8
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]

# docker build -t my