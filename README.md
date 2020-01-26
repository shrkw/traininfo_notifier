# Yahoo路線情報の運転状況をGoogle Homeに自発的に通知させる

This system creates sub process to host audio file for enabling to take by Google home.

## Develop

### Python runtime

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
