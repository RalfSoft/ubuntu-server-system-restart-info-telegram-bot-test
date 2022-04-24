# Ubuntu server system restart info with a telegram-bot

This will check on your ubuntu server if a reboot is required and sends you a telegram message.
To start use the **docker-compose.yml** file.
Check that your Telegram Bot API Keys isn't used by another script.
https://api.telegram.org/botYOUR_TELEGRAM_BOT_API_KEY/getUpdates should return:

```ok: true```

----------------------------------------------------

If your system isn't supported clone the Github repository and add 
```
build: ./
``` 
instead of 
```
image: sonn567/ubuntu-server-system-restart-info-telegram-bot:latest
```
in the ```docker-compose.yml```.
Now run ```docker-compose up -d``` and the docker image will be built for your system.
