FROM python:3.10.0-alpine as builder

WORKDIR /usr/app
ENV PATH="/usr/app/venv/bin:$PATH"
COPY src/requirements.txt requirements.txt
RUN \
    # These libraries are needed for the psycopg2 module
    apk add --no-cache postgresql-libs musl-dev && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev libffi-dev musl-dev && \
    python -m venv /usr/app/venv && \
    source /usr/app/venv/bin/activate && pip install -r requirements.txt && \
    apk --purge del .build-deps

# FROM python:3.10-slim@sha256:2bac43769ace90ebd3ad83e5392295e25dfc58e58543d3ab326c3330b505283d
# # copy only the dependencies installation from the 1st stage image
# WORKDIR /app
# COPY --from=builder /usr/app/venv /usr/app/venv
COPY src /app

WORKDIR /app
# update PATH environment variable
ENV PATH="/usr/app/venv/bin:$PATH"

ENTRYPOINT [ "python3", "main.py" ]
