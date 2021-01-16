from fabric.api import cd, env, run
from fabric.contrib.files import exists
from fabric.operations import local

REPO_URL = "git@github.com:JonathanMeans/imtoodumbtofigureout531onmyown.git"


def _get_latest_source():
    if exists(".git"):
        run("git fetch")
    else:
        run(f"git clone {REPO_URL} .")
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f"git reset --hard {current_commit}")


def _update_pipenv():
    run("pipenv sync")


def _update_static_files():
    run("pipenv run python manage.py collectstatic --noinput")


def deploy():
    site_folder = f"/home/sites/{env.host}"
    run(f"mkdir -p {site_folder}")
    with cd(site_folder):
        _get_latest_source()
        _update_pipenv()
        _update_static_files()
