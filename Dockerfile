FROM python:alpine


# Install dependencies:
COPY . .
RUN pip install -r requirements.txt

# Run application
ENTRYPOINT python manage.py runserver 0.0.0.0:8000
