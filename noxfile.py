import nox

LIB_NAME = "cycloplanning"
PYTHON_ALL_VERSIONS = ["3.10", "3.11", "3.12"]
PYTHON_DEFAULT_VERSION = "3.12"


@nox.session(python=PYTHON_ALL_VERSIONS, reuse_venv=True, tags=["tests"])
def tests(session: nox.Session):
    session.install("--upgrade", "pip")
    # We need to install the package in editable mode otherwise test coverage is
    # applied to the virtualenv rather than the source directory
    session.install("-e", ".")
    session.install("pytest", "pytest-cov")
    args = session.posargs
    if session.name.endswith(PYTHON_DEFAULT_VERSION):
        args.extend(
            (
                f"--cov={LIB_NAME}",
                "--cov-config=pyproject.toml",
                "--cov-report=term",
                "--junitxml=report.xml",
                "--cov-report=xml:coverage.xml",
                "--cov-report=html",
            )
        )
    session.run("pytest", *args)
