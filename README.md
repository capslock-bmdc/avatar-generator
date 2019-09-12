## CAPSLOCK avatar generator

### setup & install
- make sure you have python 3.x installed by running `python --version` or `python3 --version`.
- run `pip install -r requirements.txt`.
- run `git clone` on this repo.
- for bot: create a file in the root dir called `.env` with the folllowing line: `export SLACK_API_TOKEN='<your-token>'`.

### run generator
- `cd` into the project directory.
- run `python generator.py` or `python3 generator.py`.
- see your generated file - `avatar.png` - in the project dir.

### run bot
- `cd` into the project directory.
- run `python bot.py` or `python3 bot.py`.
- you can now iteract with it from slack.

