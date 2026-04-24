# Docker Assignment - Simple Python App

This repository contains a simple Python app containerized with Docker.

## Project Files

- `app.py`: Simple Python application
- `Dockerfile`: Docker build instructions
- `docker-compose.yml`: Optional compose setup
- `SUBMISSION_REPORT.md`: Organized step-by-step work log

## App Code

```python
print("Hello from Docker!")
```

## Build Docker Image

```bash
docker build -t my-app .
```

## Run Container

```bash
docker run --rm --name my-app-container my-app
```

## Check Running Containers

```bash
docker ps
```

## Optional Docker Compose

```bash
docker compose up --build
```

## GitHub Push Commands

```bash
git init
git add .
git commit -m "Initial Docker assignment submission"
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```
