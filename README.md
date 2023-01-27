# FastAPI Users - Database adapter for EdgeDB

<p align="center">
  <img src="https://raw.githubusercontent.com/frankie567/fastapi-users/master/logo.svg?sanitize=true" alt="FastAPI Users">
</p>

<p align="center">
    <em>Ready-to-use and customizable users management for FastAPI</em>
</p>

[//]: # ([![build]&#40;https://github.com/fastapi-users/fastapi-users-db-edgedb/workflows/Build/badge.svg&#41;]&#40;https://github.com/fastapi-users/fastapi-users/actions&#41;)
[//]: # ([![codecov]&#40;https://codecov.io/gh/fastapi-users/fastapi-users-db-edgedb/branch/master/graph/badge.svg&#41;]&#40;https://codecov.io/gh/fastapi-users/fastapi-users-db-edgedb&#41;)
[//]: # ([![PyPI version]&#40;https://badge.fury.io/py/fastapi-users-db-edgedb.svg&#41;]&#40;https://badge.fury.io/py/fastapi-users-db-edgedb&#41;)
[//]: # ([![Downloads]&#40;https://pepy.tech/badge/fastapi-users-db-edgedb&#41;]&#40;https://pepy.tech/project/fastapi-users-db-edgedb&#41;)

---

**Documentation**: <a href="https://fastapi-users.github.io/fastapi-users/" target="_blank">https://fastapi-users.github.io/fastapi-users/</a>

**Source Code**: <a href="https://github.com/fastapi-users/fastapi-users" target="_blank">https://github.com/fastapi-users/fastapi-users</a>

---

Add quickly a registration and authentication system to your [FastAPI](https://fastapi.tiangolo.com/) project. **FastAPI Users** is designed to be as customizable and adaptable as possible.

**Sub-package for EdgeDB support in FastAPI Users.**

## Development

### Setup environment

You should create a virtual environment and activate it:

```bash
python -m venv venv/
```

```bash
source venv/bin/activate
```

And then install the development dependencies:

```bash
make install
```

### Run unit tests

You can run all the tests with:

```bash
make test
```

Alternatively, you can run `pytest` yourself:

```bash
pytest
```

There are quite a few unit tests, so you might run into ulimit issues where there are too many open file descriptors. You may be able to set a new, higher limit temporarily with:

```bash
ulimit -n 2048
```

### Format the code

Execute the following command to apply `isort` and `black` formatting:

```bash
make format
```

## License

This project is licensed under the terms of the MIT license.
