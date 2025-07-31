# FROM node:18-alpine 

# WORKDIR /app

# COPY package*.json ./
# RUN npm ci 
# COPY . .
# RUN npm run build 
# #RUN npm install -g serve 
# EXPOSE 3000

# #CMD ["yarn", "start"]
# CMD ["npm","run","dev"]

# Stage 1: Build React app
FROM node:18 AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:alpine

# Copy built React files to Nginx's html directory
COPY --from=builder /app/build /usr/share/nginx/html

# Optional: Replace default Nginx config if needed
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

