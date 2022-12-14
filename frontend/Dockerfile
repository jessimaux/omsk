FROM node:18-alpine
WORKDIR /app

COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

CMD ["npm", "run", "dev"]