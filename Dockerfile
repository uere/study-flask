FROM  python:3.7.3
MAINTAINER Uere Mizera "ueremizera@gmail.com"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
