FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3 python3-pip -y

RUN pip3 install flask
RUN pip3 install gunicorn
RUN pip3 install requests
RUN pip3 install bs4
RUN pip3 install janome
RUN pip3 install nltk
RUN pip3 install pytest
RUN pip3 install urllib3
RUN pip3 install certifi

RUN mkdir /src

CMD flask run
