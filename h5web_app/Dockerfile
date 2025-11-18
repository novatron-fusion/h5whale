FROM node:22-slim AS base

ARG H5WEB_APP_PORT=3000
ARG VITE_HSDS_URL=http://localhost:31415
ARG VITE_HSDS_USER=admin
ARG VITE_HSDS_PASSWORD=admin

ENV H5WEB_APP_PORT=${H5WEB_APP_PORT}
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

EXPOSE $H5WEB_APP_PORT
CMD pnpm preview --port $H5WEB_APP_PORT --host