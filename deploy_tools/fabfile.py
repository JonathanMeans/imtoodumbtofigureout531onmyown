import random

from fabric.api import cd, env, run
from fabric.contrib.files import exists, append
from fabric.operations import local

REPO_URL = "git@github.com:JonathanMeans/imtoodumbtofigureout531onmyown.git"


def _get_latest_source():
    if exists(".git"):
        run("git fetch")
    else:
        run(f"git clone {REPO_URL} .")
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f"git reset --hard {current_commit}")


def _update_virtualenv():
    if not exists("virtualenv/bin/pip"):
        run("python3.8 -m venv virtualenv")
    run("./virtualenv/bin/pip install -r requirements.txt")


def _create_or_update_dotenv():
    append(".env", "DJANGO_DEBUG_FALSE=y")
    append(".env", f"SITENAME={env.host}")
    current_contents = run("cat .env")
    if "DJANGO_SECRET_KEY" not in current_contents:
        new_secret = "".join(
            random.SystemRandom().choices("abcdefghijklmnopqrstuvwxyz0123456789", k=50)
        )
        append(".env", f"DJANGO_SECRET_KEY={new_secret}")


def _update_static_files():
    run("virtualenv/bin/python manage.py collectstatic --noinput")


def deploy():
    site_folder = f"/home/sites/{env.host}"
    run(f"mkdir -p {site_folder}")
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
