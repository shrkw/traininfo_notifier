# Yahoo路線情報の運転状況をGoogle Homeに自発的に通知させる

This system creates sub process to host audio file for enabling to take by Google home.

## Develop

use VS Code Remote development extension.

## Deploy

```bash
sudo apt-get -y install git python3-pip
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
git clone git@github.com:shrkw/traininfo_notifier.git
cd traininfo_notifier
python3 -m venv .venv && ~/.poetry/bin/poetry install --no-dev
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
cd /home/pi/traininfo_notifier; GOOGLE_APPLICATION_CREDENTIALS=xxx1 FRIENDLY_NAME=xxx2 TRAIN_INFO_URL=https://transit.yahoo.co.jp/traininfo/detail/xxx/ poetry run python main.py
```
