FROM tiangolo/uwsgi-nginx-flask:python3.9

ARG APP_ENV=production

WORKDIR /app

COPY /docker/flask/requirements.txt ./requirements.txt

# For development, Jupyter remote kernel, Hydrogen
# Using inside the container:
# jupyter notebook --ip=0.0.0.0 --allow-root
RUN bash -c "if [ $APP_ENV == 'development' ] ; \
then echo -e '\r\njupyter' >> requirements.txt ; \
fi"
EXPOSE 8888

RUN pip install --no-cache-dir -r requirements.txt

# For prod:
# COPY /app/flask /app

COPY /docker/nginx/conf /etc/nginx/conf.d/
EXPOSE 5000

EXPOSE 80