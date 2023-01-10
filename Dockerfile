FROM ubuntu:18.04

WORKDIR /bot
RUN chmod 777 /bot


RUN apt -qq update
RUN apt -qq install -y python3 python3-pip locales megatools
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
COPY requirements.txt /requirements.txt
RUN cd /

RUN pip3 install -U -r requirements.txt
RUN mkdir /LazyDeveloper
WORKDIR /LazyDeveloper
COPY start.sh /start.sh

# RUN chmod +x aria.sh

CMD ["/bin/bash", "/start.sh"]
