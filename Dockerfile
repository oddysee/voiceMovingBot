FROM python:latest
LABEL Name=voicemovingbot Version=0.0.1 
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD . /code
WORKDIR /code
EXPOSE 5000
CMD ["python", "src/start.py"]
