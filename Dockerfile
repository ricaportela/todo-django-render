FROM python:3.10.5

ENV PYTHONUNBUFFERED 1

# Create the virtual environment
RUN python -m venv /venv

# Activate the virtual environment
ENV VIRTUAL_ENV /venv
ENV PATH /venv/bin:$PATH

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/

# Install dependencies inside the virtual environment
RUN pip install -r requirements.txt

COPY . /app/

# Copy static files to the static files directory
RUN python manage.py collectstatic --no-input

EXPOSE 8000
