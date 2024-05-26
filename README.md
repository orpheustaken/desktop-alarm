<div align="center">
  <h1>Yet another poorly written Alarm Manager</h1>
  <p><i>Because I have serious problems waking up too early in the morning</i></p>
</div>

[![Black](https://img.shields.io/badge/code%20style-black-000000)](https://github.com/ambv/black)

### Dependencies

Besides the most recent version of Python, Pip and what is listed in `requirements.txt`, the following packages must also be installed:

* cowsay
* figlet
* fortune
* mpv

![desktop_alarm](https://user-images.githubusercontent.com/63078965/175437725-9f3faa24-040f-48c6-8665-e5b7e457f625.png)

### Installation on Arch Linux

After cloning the repository, first create a Virtual Enviroment:

```console
python -m venv venv
```

Then, the activate script must be sourced:

```console
source ./venv/bin/activate
```

Already inside the venv, install the Python Dependencies:

```console
pip install -r requirements.txt
```

Finally, the System Dependencies can be installed:

```console
sudo pacman -S cowsay figlet fortune-mod mpv
```

To run the Alarm, simply execute `alarm_main.py`:

```console
cd src/app/
python __main__.py
```
