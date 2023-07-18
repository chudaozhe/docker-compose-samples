FROM php:8.1.9-fpm

WORKDIR /notebooks

COPY ./php-zmq /usr/src/php/ext/php-zmq

RUN apt-get update \
  && apt-get install -y python3-pip zlib1g-dev libzmq3-dev libzip-dev \
  && pip3 install jupyterlab \
  && docker-php-ext-install zip php-zmq \
  && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

ENV PATH="/root/.composer/vendor/bin:$PATH"

RUN composer global require rabrennie/jupyter-php-kernel \
  && jupyter-php-kernel --install \
  && jupyter-lab --generate-config

CMD ["jupyter", "lab", "--allow-root", "--ip=0.0.0.0", "--LabApp.token=''", "--notebook-dir=/notebooks"]
