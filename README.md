## About

A functional Discord bot to make your life easier. Set reminders, twitter alerts, and more!

## Commands

| Command   | Description                                                                                                                                  | Usage              | Examples                                     |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------------------|
| $avatar   | Get the avatar of yourself or another user.<br />Works for any user on discord.                                                              | $avatar (user)     | **$avatar**<br />**$avatar User#0001**       |
| $cat      | Get a random cat picture.                                                                                                                    | $cat               | **$cat**                                     |
| $flip     | Flip a coin.                                                                                                                                 | $flip              | **$flip**                                    |
| $password | Generates and Direct Messages you a URL safe password of specified length.                                                                   | $password (#bytes) | **$password 18**                             |
| $remind   | Set a reminder after a set countdown.<br />May use intervals of seconds, minutes, ... months, years.<br />User is pinged in the server used. | $remind            | **$remind 1 day Delete fortnite**            |
| $remindm  | Similar to $remind except the user is Direct Messaged on discord.                                                                            | $remindm           | **$remindm 2 hr Play fortnite**              |
| $tweet    | Get alerted whenever the specified twitter account tweets.                                                                                   | $tweet (account)   | **$tweet BarackObama**<br />**$tweet @jack** |

## Dependencies

If you would like to use this bot yourself, install the following:

1. **Python**

2. **[discord.py](https://discordpy.readthedocs.io/en/stable/)**

    Use this command on **\*nix systems** to install **<span>discord.py</span>:**

    `python3 -m pip install -U discord.py`

    If you are using **Windows**, then the following should be used instead:

    `py -3 -m pip install -U discord.py`

3. **dotenv**

    Similar to **discord.py**, use command `python3 -m pip install -U python-dotenv` on **\*nix systems**

    And `py -3 -m pip install -U python-dotenv` for **Windows**.

    Register a discord bot [here](https://discordapp.com/developers/applications/me)

    And copy the token:

    <img src="https://www.freecodecamp.org/news/content/images/2021/06/image-122.png" alt="Image_Token_Example" width="500"/>

    Then write your token in a **.env** file in the root directory formatted as following:
    ```
    TOKEN=your token here
    ```
