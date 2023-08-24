# Pants & Poetry monorepo

This is a monorepo where there are several subprojects in `py/release-*/projects/` and a top-level virtual project (for each `pants` resolve) that has a `pyproject.toml` and `poetry.lock` file.
Each workspace gets it's own dependency group so if you want to install a single workspace (e.g. to run unit tests in CI) you can run `poetry install --only cli` which will install `cli` and `lib` (because `cli` depends on it).
If you run `poetry install` you get all groups which is probably what you want for local development.

This monorepo also supports `sandbox` projects which are ignored by `pants` by can install libs using _path dependencies_
