FROM python:3.11.7-slim-bullseye as builder

ENV PYTHONUNBUFFERED=1
WORKDIR /platform/modules
COPY . .

RUN apt-get update
RUN python -m venv /venv
RUN /venv/bin/pip install --no-cache-dir --upgrade pip setuptools
RUN /venv/bin/pip install -r requirements.txt
RUN /venv/bin/pip install -U xformers --index-url https://download.pytorch.org/whl/cu118

FROM python:3.11.7-slim-bullseye as app

COPY --from=builder /venv /venv
ENV VIRTUAL_ENV=/venv

ENV PATH="/venv/bin:$PATH"
