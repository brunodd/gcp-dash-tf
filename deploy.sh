gcloud run deploy dash-demo \
--image=europe-west1-docker.pkg.dev/my-demo-project-yuhijk/dash-repo/dash-demo:latest \
--platform=managed \
--project=my-demo-project-yuhijk \
--region=europe-west1 \
--timeout=60 \
--concurrency=10 \
--cpu=1 \
--max-instances=4 \
--allow-unauthenticated




