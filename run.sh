if [ ! -d "/usr/bin/python3" ]; then
    cd /var/www/pomodoro-work-cycle && python3 main.py
else
  cd /var/www/pomodoro-work-cycle && python main.py
fi
