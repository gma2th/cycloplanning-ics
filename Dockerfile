FROM --platform=linux/amd64 python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uvkk

RUN --mount=source=dist,target=/dist uv pip install --system --no-cache /dist/*.whl

CMD cycloplanning --help
