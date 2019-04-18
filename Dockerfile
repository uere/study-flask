FROM  python:3.7.3-alpine3.9
MAINTAINER Uere Mizera "ueremizera@gmail.com"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod 644 app.py
ENTRYPOINT ["python"]
CMD ["app.py"]
