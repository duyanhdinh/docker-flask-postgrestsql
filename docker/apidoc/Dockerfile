FROM node:17-alpine

WORKDIR /app

RUN yarn global add apidoc

COPY ./app .

ENTRYPOINT ["apidoc", "-i", "/app/flask", "-o"]