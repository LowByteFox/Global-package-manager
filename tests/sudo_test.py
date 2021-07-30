import os, subprocess
from getpass import getpass

def is_root():
    return os.geteuid() == 0

def test_sudo(pwd=""):
    args = "sudo -S echo OK".split()
    kwargs = dict(stdout=subprocess.PIPE,
                  encoding="ascii")
    if pwd:
        kwargs.update(input=pwd)
    cmd = subprocess.run(args, **kwargs)
    return ("OK" in cmd.stdout)

def prompt_sudo():
    ok = is_root() or test_sudo()
    if not ok:
        pwd = getpass("password: ")
        ok  = test_sudo(pwd)
    return ok

if prompt_sudo():
   os.system("sudo pacman -Syy")
else:
    print("Access denied !")