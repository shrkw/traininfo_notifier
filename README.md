# Yahoo路線情報の運転状況をGoogle Homeに自発的に通知させる

This system uses 2 processes:

* A: Scrape train info and generate audio file
  * kicked by crond
* B: Audio file hosting server

## Develop

### pyenv and pythons

```bash
VERSION=3.8.0
```


```bash
brew install pyenv
brew install zlib sqlite
export LDFLAGS="${LDFLAGS} -L/usr/local/opt/zlib/lib"
export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/zlib/include"
export LDFLAGS="${LDFLAGS} -L/usr/local/opt/sqlite/lib"
export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/sqlite/include"
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/zlib/lib/pkgconfig"
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/sqlite/lib/pkgconfig"
```

```bash
pyenv install ${VERSION}
```

### pipenv

```bash
brew install pipenv
PIPENV_VENV_IN_PROJECT=true pipenv --python=$(pyenv root)/versions/${VERSION}/bin/python install
```

## Deploy

install git and pip at first.

```bash
pip3 install pipenv
git clone git@github.com:shrkw/traininfo_notifier.git
cd traininfo_notifier
PIPENV_VENV_IN_PROJECT=true pipenv install
```

## Run

### Process 1: File Hosting Process

```bash
cd traininfo_notifier
pipenv run python -m http.server
```

### Process 2: Main Process

### Env vars

Make sure you have valid GCP access.

* GOOGLE_APPLICATION_CREDENTIALS
* FRIENDLY_NAME
* SERVER_HOST
* TRAIN_INFO_URL

```bash
cd /home/pi/traininfo_notifier; GOOGLE_APPLICATION_CREDENTIALS=xxx1 FRIENDLY_NAME=xxx2 SERVER_HOST=192.168.1.xxx:8000 TRAIN_INFO_URL=https://transit.yahoo.co.jp/traininfo/detail/xxx/ pipenv run python main.py
```
