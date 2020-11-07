FROM ubuntu:20.04

RUN apt-get update
RUN apt-get -y install python3-pip git

RUN git clone https://github.com/waleedhammam/national_id.git
RUN cd national_id && pip3 install -r requirements.txt

EXPOSE 8001
CMD cd /national_id/ && python3 server.py