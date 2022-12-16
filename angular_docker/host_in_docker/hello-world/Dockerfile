# STAGE 1: Build ###
FROM node:12.7-alpine AS build
RUN npm run build
# STAGE 2: Run ###
FROM nginx:1.17.1-alpine
COPY ./dist/cx-compass-request-ui /usr/share/nginx/html