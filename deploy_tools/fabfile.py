from fabric.contrib.files import append, exists, sed
from fabric.api import cd, env, local, run
import random


REPO_URL = 'https://github.com/ibrobabs/tdd.git'
env.user = "ubuntu"
env.key_filename = ["/home/ibrokola/Desktop/TDD/anotherweb.pem"]
env.host = ["ec2-34-237-245-176.compute-1.amazonaws.com"]

def deploy():
    site_folder = f'/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_settings(env.host)
        _update_virtualenv()
        _update_static_files()
        _update_database()



def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'git reset --hard {current_commit}')


def _update_settings(site_name):
    settings_path = 'babs/settings.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path, 
        'ALLOWED_HOST =.+$',
        f'ALLOWED_HOSTS = ["{site_name}"]'
    )
    secret_key_file = 'babs/secret_key.py'
    if not exist(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().chioces(chars, k=50))
        append(secret_key_file, f'SECRET_KEY = "{key}"')
    append(settings_path, '\nfrom.secret_key import SECRET_KEY')


def _update_virtualenv():
    if not exists('virtualenv/bin/pip'):
        run(f'python3.6 -m venv virtualenv')
    run('./virtualenv/bin/pip install -r requirements.txt')



def _update_static_files():
    run('./virtualenv/bin/python manage.py collectstatic --noinput')


def _update_database():
    run('./virtualenv/bin/python manage.py migrate --noinput')

