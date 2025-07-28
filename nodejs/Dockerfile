# Base image
FROM node:18

# Create app directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy rest of the files
COPY . .

# Expose port
EXPOSE 3000

# Command to run the app
CMD [ "npm", "start" ]
