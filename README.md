# web_pwm
A tool to use the Orange Pi PWM via a web interface.

## How to run
```bash
sudo pip3 install flask OrangePi.GPIO
sudo flask run --host=0.0.0.0
```

The app was written for the Orange Pi board, but it probably would be compatible with Raspberry Pi after some changes.

## Problems
Because this project was written as a one-time tool for my personal use, there are some problems with it.

- Hard-coded pin numbers
- Because you need to be root to manipulate GPIO, you have to run ``flask run`` with sudo and therefore install flask as root too (``sudo pip3 install ...``).
  I've read something about setting some permissions so you don't have to be root, but it seemed to complicated. Maybe in the future?
- You probably shouldn't use ``flask run`` as a normal server, but I can't imagine anyone using this in production, so I guess it may be fine
