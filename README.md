# Docker Assignment - Calculator App

This repository contains a small Python calculator app containerized with Docker.

## Project Files

- `app.py`: Calculator CLI application
- `Dockerfile`: Docker build instructions
- `docker-compose.yml`: Optional compose setup
- `SUBMISSION_REPORT.md`: Organized step-by-step work log

## Calculator Operations

- `add`: addition
- `sub`: subtraction
- `mul`: multiplication
- `div`: division

## Build Docker Image

```bash
docker build -t my-app .
```

## Run Container (Interactive - Continuous)

Run this to start the calculator in continuous mode. It keeps asking for input until you type `exit`.

```bash
docker run -it --rm --name my-app-container my-app
```

## Run Container (One-Shot)

```bash
docker run --rm my-app mul 7 6
# Result: 42.0

docker run --rm my-app div 9 3
# Result: 3.0
```

## Verify Container Running In Backend

Use two terminals:

1) Start calculator container in detached mode with interactive stdin:

```bash
docker run -d -i --name my-app-running my-app
```

2) Verify it is running:

```bash
docker ps
```

3) Stop and remove after verification:

```bash
docker stop my-app-running
docker rm my-app-running
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
