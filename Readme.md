## Install libs

```bash
  # pip
  sudo apt install -y python-pip
  pip install --user --upgrade pip

  # PyQt5
  pip install PyQt5 # Python 3
  sudo apt install -y python-pyqt5 # Python 2

  # gtts
  pip install gTTS
  python -m pip install --upgrade gtts
  python -m pip install --upgrade gtts-token

  # playsound
  pip install playsound
```

<hr/>

## Run
```bash
  python main.py
```

## Create terminal command
```bash
  sudo ln -s /var/www/pomodoro-work-cycle/run.sh /usr/local/bin/pomodoro-tech
```

## Run as a process
```bash
  pomodoro-tech &
```
