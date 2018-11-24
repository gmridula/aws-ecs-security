FROM node:argon

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install

# Bundle app source
COPY sample.js /usr/src/app/

#CMD [ "node", "sample.js" ]
ENTRYPOINT ["./cron.sh"]
