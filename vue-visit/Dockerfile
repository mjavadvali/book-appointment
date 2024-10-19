FROM node:18-alpine

WORKDIR /app

RUN rm -rf node_modules package-lock.json

COPY package*.json ./

RUN npm install axios
RUN npm install

COPY . .

EXPOSE 5173

