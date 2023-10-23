FROM node:12.18.4-alpine3.9 as builder
WORKDIR /app
COPY . .
RUN yarn install && yarn build

FROM nginx:1.21.3
COPY --from=builder /app/dist /var/www/html
WORKDIR /var/www/html

#docker build -t chudaozhe/alarm-dog-fe:1.0.0-v1.1 .