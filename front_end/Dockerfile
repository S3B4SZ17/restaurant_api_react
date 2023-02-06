# syntax=docker/dockerfile:1

FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app

# Copy our node module specification
COPY package.json package.json
COPY package-lock.json package-lock.json

# install node modules and build assets
RUN npm config set legacy-peer-deps true && npm i --save --legacy-peer-deps && npm install react-bootstrap bootstrap && \
 npm install axios && npm install react-router-dom && npm install -g npm-check-updates && npm install @material-ui/core --legacy-peer-deps && \
 npm install @material-ui/icons --legacy-peer-deps && npm install @mui/material --legacy-peer-deps && npm install @mui/icons-material --legacy-peer-deps && \
 npm install styled-components --legacy-peer-deps && npm install @emotion/react --legacy-peer-deps && npm install @emotion/styled --legacy-peer-deps && \
 npm install mdb-react-ui-kit --legacy-peer-deps && npm install react-cookie --legacy-peer-deps && npm i @monaco-editor/react --legacy-peer-deps && \
 npm i @fortawesome/fontawesome-free --legacy-peer-deps && npm i react-hot-toast --legacy-peer-deps

# Copy all files from current directory to working dir in image
# Except the one defined in '.dockerignore'
COPY . .

# Create production build of React App
RUN yarn build

# Choose NGINX as our base Docker image
FROM nginx:alpine

# Set working directory to nginx asset directory
WORKDIR /usr/share/nginx/html

# Remove default nginx static assets
RUN rm -rf *

# Copy static assets from builder stage
COPY --from=builder /app/build .

# Entry point when Docker container has started
ENTRYPOINT ["nginx", "-g", "daemon off;"]
