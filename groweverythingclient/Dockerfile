FROM node:16.13.0 AS nodejs
WORKDIR /app
# Install app dependencies
COPY package.json package-lock.json ./
RUN npm install -g @angular/cli @angular-devkit/build-angular && npm install
# RUN npm install
COPY . .

EXPOSE 4200

CMD ["npm", "start"]


# RUN npm run build --prod

# EXPOSE 80
# use nginx to serve the static files
# FROM nginx:alpine
# COPY --from=nodejs /frontend-server/dist/soil-carbon usr/share/nginx/html