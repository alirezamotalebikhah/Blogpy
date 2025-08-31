FROM python:3.8
LABEL MAINTAINER="alireza"
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH="/blog"

RUN mkdir /blog
WORKDIR /blog
COPY . /blog
ADD requirements/requirements.txt /blog
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "--bind", "0.0.0.0:9000", "--chdir", "/blog", "djangoProject.wsgi:application"]
