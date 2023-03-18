FROM python:3.11

WORKDIR / code
COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir


ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]