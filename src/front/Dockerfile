FROM nginx

RUN mkdir -p /etc/nginx/sites-enabled
COPY front_config /etc/nginx/sites-enabled/

RUN service nginx restart
