# Capstone Project

Demonstrates concepts from OK Coders Pro - Intro to Python course.

## Minimum Requirements

* [Python 3.13+](https://www.python.org/downloads/release/python-31311/)
* [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Setup

### Create and activate virtual environment, install dependencies

```bash
uv venv --python ">=3.13,<3.14"
source .venv/bin/activate
uv pip install -r pyproject.toml --all-extras
```

### ezgmail Secrets

Check the [ezgmail documentation](https://github.com/asweigart/ezgmail). A `credentials.json` file is needed to use ezgmail. It should be placed in the relative path to [capstone_project.py](capstone_project.py).

## Quickstart

After setting up the virtual environment and installing dependencies, run the main script with:

```bash
# default email account
uv run capstone_project.py

# specify email account
EMAIL=<your_email@gmail.com> uv run capstone_project.py
```

> [!NOTE]
> Copy the `.env.example` to a `.env` file and set the `EMAIL` variable to your Gmail address to avoid specifying it each time.

A `capstone_hn_posts.db` SQLite database file will be created in the relative path and an email will be sent to the configured Gmail account.
