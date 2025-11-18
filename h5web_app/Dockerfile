# Build stage
FROM node:22-slim AS builder

ARG VITE_HSDS_URL=http://localhost:31415
ARG VITE_HSDS_USER=admin
ARG VITE_HSDS_PASSWORD=admin

ENV VITE_HSDS_URL=${VITE_HSDS_URL}
ENV VITE_HSDS_USER=${VITE_HSDS_USER}
ENV VITE_HSDS_PASSWORD=${VITE_HSDS_PASSWORD}

ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

COPY . /h5web_app
WORKDIR /h5web_app

RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install
RUN pnpm run build

# Production stage
FROM nginx:alpine

ARG H5WEB_APP_PORT=3000

# Copy built files from builder
COPY --from=builder /h5web_app/dist /usr/share/nginx/html

# Create nginx config
RUN echo "server { \
    listen ${H5WEB_APP_PORT}; \
    listen [::]:${H5WEB_APP_PORT}; \
    root /usr/share/nginx/html; \
    index index.html; \
    location / { \
        try_files \$uri \$uri/ /index.html; \
    } \
}" > /etc/nginx/conf.d/default.conf

EXPOSE ${H5WEB_APP_PORT}

CMD ["nginx", "-g", "daemon off;"]