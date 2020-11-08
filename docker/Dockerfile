FROM ubuntu:20.04

RUN apt-get update && apt-get -y install --no-install-recommends \
    python3-pip=20.0.2-5ubuntu1.1 git=1:2.25.1-1ubuntu3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/waleedhammam/national_id.git
WORKDIR /national_id
RUN pip3 install -r requirements.txt

EXPOSE 8001
CMD python3 server.py