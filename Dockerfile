FROM python:3.11
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./entrypoint.py .
CMD exec gunicorn entrypoint:app
