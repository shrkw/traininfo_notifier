# Yahoo路線情報の運転状況をGoogle Homeに自発的に通知させる

This system creates sub process to host audio file for enabling to take by Google home.

## Develop

use VS Code Remote development extension.

## Deploy

install git and pip at first.

```bash
pip3 install pipenv
git clone git@github.com:shrkw/traininfo_notifier.git
cd traininfo_notifier
PIPENV_VENV_IN_PROJECT=true pipenv install
```

I let this run on Raspbian and lxml is installed by apt.

<https://raspberrypi.stackexchange.com/questions/68894/cant-install-lxml>

## Run

### Env vars

Make sure you have valid GCP access.

* GOOGLE_APPLICATION_CREDENTIALS
* FRIENDLY_NAME
* TRAIN_INFO_URL

```bash
cd /home/pi/traininfo_notifier; GOOGLE_APPLICATION_CREDENTIALS=xxx1 FRIENDLY_NAME=xxx2 TRAIN_INFO_URL=https://transit.yahoo.co.jp/traininfo/detail/xxx/ pipenv run python main.py
```
