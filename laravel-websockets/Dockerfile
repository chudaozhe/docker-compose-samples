FROM php:8.1.9-cli
WORKDIR /var/www/app
RUN apt-get update && apt-get install -y unzip \
    && docker-php-ext-install pdo_mysql \
    && curl -sfL https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer \
    && chmod +x /usr/bin/composer \
    && composer self-update 2.3.10 \
    && composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/

EXPOSE 6001

#app目录为项目目录
COPY ./app .

CMD php artisan websockets:serve