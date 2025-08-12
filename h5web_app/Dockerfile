FROM node:22-slim AS base

ARG H5WEB_APP_PORT=3000
ARG H5GROVE_APP_URL=http://localhost
ARG H5GROVE_APP_PORT=8888
ENV H5WEB_APP_PORT=${H5WEB_APP_PORT}
ENV VITE_H5GROVE_URL=${H5GROVE_APP_URL}
ENV VITE_H5GROVE_PORT=${H5GROVE_APP_PORT}
# FIXED URL - Always point to nginx proxy (runtime switching handled by nginx)
ENV VITE_HSDS_URL=http://localhost:31415
ENV VITE_HSDS_USER=admin
ENV VITE_HSDS_PASSWORD=admin

ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable
COPY . /h5web_app
WORKDIR /h5web_app

RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install
RUN pnpm run build

EXPOSE $H5WEB_APP_PORT
CMD pnpm preview --port $H5WEB_APP_PORT --host