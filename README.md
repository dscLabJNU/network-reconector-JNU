# Auto login for campus network of JNU

This tool provides the automatic reconnection function of campus network.



# Configuration
To prevent blocking, use the account pool to login in to the campus network.

First create a configuration file `config.py` in the root directory.

Then, add a dictionary named `ACCOUNT_POOL` into `config.py`, as `ACCOUNT_POOL:{${id}:{${username}:${passwd}}}`, where `${id}` is just an identify for an account, `${username}` indicates the `username` and `${passwd}` is the `passwd` of each campus account.


After that, just download a chrome driver [on this website](http://chromedriver.storage.googleapis.com/index.html), and move it into `./driver` directory (create the directory if necessary).

**Please Make sure the version between the driver and your chrome is the same.**



# Usage

Create a new python virtual environment and install the dependencies needed with `python3 install -r requirements.py`

Then activate the autologin script with `sudo python3 autologin.py`

A chrome-monitored window will open, simulating login behavior.