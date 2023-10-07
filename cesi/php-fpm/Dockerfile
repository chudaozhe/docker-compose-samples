FROM php:8.1.9-fpm
RUN apt-get update && apt-get install -y supervisor
CMD supervisord -c /etc/supervisor/supervisord.conf \
    && php-fpm

