# Python web-scraper

[![N|Solid](https://i.postimg.cc/6Qnkq1Qp/whimelan.png)](https://github.com/whimelan)

### Files of parser

```
current_dir
├── parsing.py    // this is a project's main file
└── sites_list.py // created apart sites array file
```

### Installation

First, you need Python (preferably >= 3 version ), download it [here](https://www.python.org/downloads/) or using [Brew](https://brew.sh) via

```
$ brew install python
```

Next we're going to create [venv](https://docs.python.org/3/library/venv.html)

# Write in Bash shell

```
python3 -m venv env

source env/bin/activate
```

# Before installing modules, we need to install pip

Right click on [this](https://bootstrap.pypa.io/get-pip.py) link and save this file in the project directory

Install pip:

```
python get-pip.py
```

# After activating venv and installing pip, start installing modules via pip

```
python3 -m pip install colorama requests_html itertools
```

# Prepare your sites list for parsing

Put your raw url-addresses (like example.com, not https://example.com) into list in sites_list.py:

```
list = [
    'example.com',
    'example.com',
    'example.com',
]
```

### Try to parse:

```
python3 parsing.py

or

python parsing.py
```

### Get the result in emails.md

But we need to understand that:

1. This script is not the best, it's just a working solution for fast scraping
2. Sometimes while using this nice regular expression you can get strings like "//cdn" or "-27@4x-32x32.png" and other junk, just delete it or ignore it
3. This script can parse JavaScript-rendered sites, uncomment some code to use this, but you can get very high load if you are going to parse over 50 sites.
4. I am not responsible for getting some data from closed sources, use it on your own risk!

### Thanks for reading and using, feel free to inform me about issues or bugs, may be I'll fix it someday and give you the best solution!
