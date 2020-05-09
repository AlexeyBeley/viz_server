FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir -p /etc/nginx/sites-enabled
COPY front_config.conf /etc/nginx/sites-enabled/


RUN service nginx restart
