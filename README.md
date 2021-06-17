## About

A functional discord bot to make your life easier. Set reminders, twitter alerts, and more!

## Commands

| Command | Description                                 | Usage          | Examples                      |
|---------|---------------------------------------------|----------------|-------------------------------|
| $avatar | Get the avatar of yourself or another user. | $avatar (user) | $avatar                       |
|         | Works for any user on discord.              |                | $avatar User#0001             |
| $cat    | Get a random cat picture.                   | $cat           | $cat                          |
| $flip   | Flip a coin.                                | $flip          | $flip                         |
| $remind | Set a reminder.                             | $remind        | $remind 1 day Delete fortnite |

## Dependencies

If you would like to edit this bot yourself, install the following:

1. **Python**

2. **[discord.py](https://discordpy.readthedocs.io/en/stable/)**

* Use this command on **\*nix systems** to install **<span>discord.py</span>:**

* `python3 -m pip install -U discord.py`

* If you are using **Windows**, then the following should be used instead:

* `py -3 -m pip install -U discord.py`

3. **dotenv**

Similar to **discord.py**, use command `python3 -m pip install -U python-dotenv` on **\*nix systems**

And `py -3 -m pip install -U python-dotenv` for **Windows**.

Write your token in a **.env** file in the root directory formatted as following:
```
TOKEN=your token here
```
