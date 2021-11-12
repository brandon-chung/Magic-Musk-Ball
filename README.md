# Magic-Musk-Ball

## Setup
- Activate venv with `/venv/bin/activate` on linux
- Set up mongo database by running `python /Backend/mongo/setup.py`
- Gather tweets by running `python /Backend/script.py`
  - The script will save the date when tweets were last gathered, so next time the script is run, only tweets after that date will be gathered
- Run web app with `uvicorn main:app`
  - Add `--reload` to command if running web app for development