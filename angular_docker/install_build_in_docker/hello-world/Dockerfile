FROM node:12.7-alpine AS build
WORKDIR /usr/src/app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build
FROM nginx:1.17.1-alpine
COPY --from=build /usr/src/app/dist/hello-world /usr/share/nginx/html