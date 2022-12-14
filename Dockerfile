FROM python:3.9
#RUN apt update
# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Mounts the application code to the image
COPY djangoProject djangoProject
ADD .env /env_file/.env
#ARG destination = "C:\Users\rogev\Documents\!Учеба\!Дз\Архитектура развертывания\курсач\djangoProject"
WORKDIR C:/Users/rogev/Documents/!Учеба/!Дз/Архитектура развертывания/курсач/djangoProject
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
#EXPOSE 8000