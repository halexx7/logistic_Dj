FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt && pip install Pillow
RUN pip install isort && pip install black
RUN pip install social_auth_app_django
COPY . /code/
