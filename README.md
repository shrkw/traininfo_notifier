# Yahoo路線情報の運転状況をGoogle Homeに自発的に通知させる




## Run

This system uses 2 processes:

* A: Scrape train info and generate audio file
    * kicked by crond
* B: Audio file hosting server




pipenv run python -m http.server

## Develop


### pyenv and pythons

```
VERSION=3.8.0
```


```
brew install pyenv
brew install zlib sqlite
export LDFLAGS="${LDFLAGS} -L/usr/local/opt/zlib/lib"
export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/zlib/include"
export LDFLAGS="${LDFLAGS} -L/usr/local/opt/sqlite/lib"
export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/sqlite/include"
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/zlib/lib/pkgconfig"
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/sqlite/lib/pkgconfig"
```

```
pyenv install ${VERSION}
```

### pipenv

```
brew install pipenv
PIPENV_VENV_IN_PROJECT=true pipenv --python=$(pyenv root)/versions/${VERSION}/bin/python install
```

## Deploy

## Run


## References

