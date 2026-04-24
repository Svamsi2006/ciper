# Assignment Submission Report

## Student Task Summary

Build a simple app, containerize it using Docker, run it, verify with `docker ps`, and push all files to GitHub with proof screenshots.

## What Was Created

1. Simple Python app in `app.py`
2. Docker setup in `Dockerfile`
3. Optional compose file in `docker-compose.yml`
4. Project documentation in `README.md`
5. This organized report in `SUBMISSION_REPORT.md`

## Step-by-Step Work Done

### Step 1: Created a Simple Application

File: `app.py`

```python
print("Hello from Docker!")
```

### Step 2: Added Dockerfile

File: `Dockerfile`

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
CMD ["python", "app.py"]
```

### Step 3: Build Docker Image

Command to run:

```bash
docker build -t my-app .
```

Expected result:
- Build completes successfully.

Screenshot required:
- Screenshot #1 showing successful Docker build output.

### Step 4: Run the Container

Command to run:

```bash
docker run --rm --name my-app-container my-app
```

Expected result:
- Terminal prints: `Hello from Docker!`

Screenshot required:
- Screenshot #2 showing app output.

### Step 5: Check Running Containers

Command to run:

```bash
docker ps
```

Expected result:
- List of running containers.
- Note: If `--rm` is used and app exits immediately, container may not appear because it stops right away.

Recommended command for screenshot clarity:

```bash
docker run -d --name my-app-running my-app sh -c "sleep 120"
docker ps
```

Screenshot required:
- Screenshot #3 showing `docker ps` output.

### Step 6: Optional Docker Compose

File: `docker-compose.yml`

```yaml
version: '3.8'
services:
  app:
    build: .
    container_name: docker-assignment-app
```

Optional run command:

```bash
docker compose up --build
```

### Step 7: Push to GitHub

Commands:

```bash
git init
git add .
git commit -m "Initial Docker assignment submission"
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

## Required Submission Items

1. GitHub repository link
2. Screenshot #1: Docker image build success
3. Screenshot #2: Container run output
4. Screenshot #3: `docker ps` output

## Final Checklist

- [x] App file created
- [x] Dockerfile created
- [x] Compose file created (optional)
- [x] README created
- [x] Submission report created
- [x] Docker commands executed successfully
- [ ] Docker build screenshot captured
- [ ] Container output screenshot captured
- [ ] `docker ps` screenshot captured
- [ ] GitHub repo created and push completed (pending GitHub login)

## Notes

If GitHub CLI (`gh`) is not installed, create the repository manually on github.com, then run the git push commands from terminal.

## Execution Evidence (Actual Results)

Executed from project directory:

1. `docker build -t my-app .`
Result: Success, image `my-app:latest` built.

2. `docker run --rm --name my-app-container my-app`
Result: Success, output was:

```text
Hello from Docker!
```

3. `docker run -d --name my-app-running my-app sh -c "sleep 120"` then `docker ps`
Result: Success, running container visible in `docker ps`:

```text
CONTAINER ID   IMAGE     COMMAND               STATUS                  NAMES
7095f75b6619   my-app    "sh -c 'sleep 120'"   Up Less than a second   my-app-running
```

4. Cleanup done:
- `docker stop my-app-running`
- `docker rm my-app-running`

5. Git repository initialized and committed:
- Commit: `3419fbc`
- Branch: `main`

6. GitHub CLI installed:
- `gh` installed at `C:\Program Files\GitHub CLI\gh.exe`
- Final blocker: interactive `gh auth login` must be completed with your GitHub account.
