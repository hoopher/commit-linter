#!/usr/bin/env python3
import os
import stat
import shutil
import pkg_resources
import sys

def enforce():
    githooks_path = pkg_resources.resource_filename(
        __name__, "hooks/commit-msg")
    user_repository = os.path.join(os.getcwd(), ".git/hooks")

    if os.path.exists(user_repository+"/commit-msg"):
        print("your repo already enforced with commit-msg hook")
    else:
        shutil.copy(githooks_path, user_repository)
        st = os.stat(user_repository + '/commit-msg')
        os.chmod(user_repository + '/commit-msg', st.st_mode | stat.S_IEXEC)
        print("Your Repo has been enforced with git commit-msg hook")

def unenforce():
    user_repository = os.path.join(os.getcwd(), ".git/hooks")
    if os.path.exists(user_repository+"/commit-msg"):
        os.remove(user_repository+"/commit-msg")
        print("The hook has been removed")
    else:
        print("The hook already does not exist")

def main():
    if not os.path.isdir('.git'):
        print('error: .git directory not found in the current path. this is not a git repository?')
        return
    githooks_path = pkg_resources.resource_filename(
        __name__, "hooks/commit-msg")

    if shutil.which('git') == None:
        print('error: git not found on path. please install git and then run pip install --upgrade commit-linter')
        return
    if not os.path.exists(githooks_path):
        print('error: git hooks template not found on %s, please run pip install commit-linter' % githooks_path)
        return
    else:
        if len(sys.argv) > 1 :
            if sys.argv[1] == "install":
                enforce()
            elif sys.argv[1] == "remove":
                unenforce()
            else:
                print("unknown command please either use:")
                print("commit-linter install ==> will install hooks to your repo")
                print("commit-linter remove ==> will remove hooks from your repo")
        else:
            print("enforcing by default")
            enforce()


if __name__ == "__main__":
    main()
