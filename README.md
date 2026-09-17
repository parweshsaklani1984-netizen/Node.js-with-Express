# Express and Flask Docker Assignment

This project contains an Express frontend and a Flask backend running as separate Docker Compose services.

## Run locally with Docker

```powershell
docker compose up --build
```

Open http://localhost:3000. The frontend serves the form and forwards submissions to Flask at `http://backend:5000/process` inside the Compose network.

## Publish images to Docker Hub

Set your Docker Hub username, log in, and build/push the images:

```powershell
$env:DOCKERHUB_USERNAME = "your-dockerhub-username"
docker login
docker compose build
docker compose push
```

The images are published as `your-dockerhub-username/assignment-frontend:latest` and `your-dockerhub-username/assignment-backend:latest`.

## Publish the code to GitHub

```powershell
git add .
git commit -m "Containerize Express frontend and Flask backend"
git push -u origin main
```