FROM nginx

RUN mkdir -p /etc/nginx/sites-enabled
COPY fb_config /etc/nginx/sites-enabled/

RUN service nginx restart
