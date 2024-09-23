FROM --platform=linux/amd64 python:slim
RUN pip install uv
RUN --mount=source=dist,target=/dist uv pip install --system --no-cache /dist/*.whl
CMD cycloplanning --help
