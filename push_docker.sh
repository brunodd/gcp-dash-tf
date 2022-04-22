#!/bin/bash

echo "Build, tag and push docker image"
docker build --platform=linux/amd64 --tag europe-west1-docker.pkg.dev/my-demo-project-yuhijk/dash-repo/dash-demo:latest -t dash-demo .

echo "Push image to GCP container registry"
docker push europe-west1-docker.pkg.dev/my-demo-project-yuhijk/dash-repo/dash-demo:latest

