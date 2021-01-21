![pypi](https://img.shields.io/pypi/v/commit-linter.svg)
![python](https://img.shields.io/pypi/pyversions/commit-linter.svg)
![license](https://img.shields.io/github/license/Hoopher/commit-linter.svg)
![last-commit](https://img.shields.io/github/last-commit/Hoopher/commit-linter.svg)
![downloads](https://img.shields.io/pypi/dm/commit-linter?style=flat-square)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/commit-linter)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/commit-linter)
![PyPI - Format](https://img.shields.io/pypi/format/commit-linter)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

# commit-linter

### An easy to use tool to that lints your commit messages according to commit conventions .

commit-linter is a Python tool that helps you standardize your commit messages to a known [commit conventions](https://www.conventionalcommits.org/en/). the tool also add emojies to your commits.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install commit-linter.

```sh
pip install commit-linter
```

## Usage

in your git repository just execute

```sh
commit-linter
```
or
```sh
commit-linter install
```
if you want to remove the hook, just execute
```sh
commit-linter remove
```

## How it works

commit-linter uses git-hooks which are scripts that exists in each repository.
Take a look at any repo you have, you will have `.git` directory, and inside you
will find `hooks` directory, commit-linter just puts a simple script named `commit-msg` 
inside that  directory and makes it executable so each time you right a commit message
it will get linted as per the conventions, you can look at script in your repository 
inside `.git/hooks` path.

Read more about [Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
This Tool is Under [MIT](https://choosealicense.com/licenses/mit/) License.