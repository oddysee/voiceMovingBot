FROM python:latest
LABEL Name=voicemovingbot Version=0.0.1 
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD . /code
WORKDIR /code
ENTRYPOINT [ "python" ]
CMD [ "src/start.py" ]