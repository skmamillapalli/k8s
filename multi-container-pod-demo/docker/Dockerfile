FROM python:latest
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app.py app.py
CMD ["python3", "app.py"]
