FROM node:14.17.0-alpine

RUN mkdir /app
WORKDIR /app

COPY ./frontend/package*.json /app/
RUN apk update && apk add bash
RUN npm install --silent

COPY ./frontend /app/

EXPOSE 3000

CMD ["/bin/bash", "/app/frontend-start.sh"]