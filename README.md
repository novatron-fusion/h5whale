# 🐳 h5whale − Docker app to explore HDF5 files

## 🚀 Quick start

- Clone the repository
- Copy the files in `data`
- Run `docker compose up`
- Access the viewer at `http://localhost:3000/?file=<name_of_your_file>`

## 📦 Repository contents

h5whale provides a Docker image to run a web application to view HDF5 files stored on an HSDS server.

- A React front-end app based on [h5web](https://github.com/silx-kit/h5web) to display and inspect HDF5 files from an HSDS server.

The app can be run with `docker compose`:

```
docker compose up
```

The viewer can be accessed at `http://localhost:3000`.

The value of the front-end app port (default: `3000`) can be changed in the `.env` file.

## 🖼️ Docker image

### Front-end for HSDS (h5web_app)

The front-end app in `h5web_app` is a React application deploying the H5Web viewer with [vite](https://vitejs.dev/) for an HSDS server

There are two .env configs for either a local hsds server on `http://localhost:5100` or for a remote server.

To start run:

- `docker compose --env-file .env.local up`
- docker compose --env-file .env.novadb up
