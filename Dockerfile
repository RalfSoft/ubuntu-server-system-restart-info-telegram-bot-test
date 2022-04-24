FROM python:3.9-alpine

RUN apk update && apk upgrade
RUN apk add build-base
RUN python3.9 -m pip install --upgrade pip

COPY bot.py /bot/bot.py
COPY entrypoint.sh /entrypoint.sh
COPY requirements.txt /tmp/requirements.txt

RUN chmod +x /entrypoint.sh
RUN python3.9 -m pip install -r /tmp/requirements.txt

ENTRYPOINT [ "/entrypoint.sh" ]

# docker build -t sonn567/ubuntu-server-system-restart-info-telegram-bot:TAG .
# docker push sonn567/ubuntu-server-system-restart-info-telegram-bot:TAG
# docker manifest create sonn567/ubuntu-server-system-restart-info-telegram-bot --amend sonn567/ubuntu-server-system-restart-info-telegram-bot:1.1.0.amd64 --amend sonn567/ubuntu-server-system-restart-info-telegram-bot:1.1.0.arm64v8
# docker manifest push sonn567/ubuntu-server-system-restart-info-telegram-bot:latest
