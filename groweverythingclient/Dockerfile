FROM node:16.13.0 AS nodejs
WORKDIR /frontend-server
# Install app dependencies
COPY package.json package-lock.json ./
RUN npm install
COPY . .

EXPOSE 80

CMD ["npm", "start"]


# RUN npm run build --prod

# EXPOSE 80
# use nginx to serve the static files
# FROM nginx:alpine
# COPY --from=nodejs /frontend-server/dist/soil-carbon usr/share/nginx/html