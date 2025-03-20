# traders_guild_applications
Microservices and application repository


# FastAPI App Deployment

## 1️⃣ Build and Push to Google Artifact Registry

```sh
docker build -t fastapi:latest .
docker tag fastapi:latest europe-west2-docker.pkg.dev/YOUR_GCP_PROJECT/traders-guild/fastapi:latest
docker push europe-west2-docker.pkg.dev/YOUR_GCP_PROJECT/traders-guild/fastapi:latest