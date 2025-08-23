FROM python:3.8
LABEL MAINTAINER="alireza"
ENV PYTHONUNBUFFERED 1
RUN mkdir /blog
WORKDIR /blog
COPY . /blog
ADD requirments/requirments.txt /blog
RUN pip install --upgrade pip
RUN pip install -r requirments.txt

RUN python manage.py collectstatic  --no input
CMD ["gunicorn" ,"--chdir" , "blog", "--bind" , ":8000" , "blogpy.wsgi:application"]