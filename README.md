# Auto login for campus network of JNU

This tool provides the automatic reconnection function of campus network.



# Configuration

First create a configuration file `config.py` in the root directory.

Then, add parameter `CAMPUS_NETWORK_USERNAME` and parameter  `CAMPUS_NETWORK_PASSWORD` to the config file

`CAMPUS_NETWORK_USERNAME` indicates the `username` and `CAMPUS_NETWORK_PASSWORD` is the `passwd` of your campus account.

After that, just download a chrome driver [on this website](http://chromedriver.storage.googleapis.com/index.html), and move it into `./driver` directory.

**Please Make sure the version between the driver and your chrome is the same.**



# Usage

Create a new python virtual environment and install the dependencies needed with `python3 install -r requirements.py`

Then activate the autologin script with `sudo python3 autologin.py`

A chrome-monitored window will open, simulating login behavior.