PROJECT_ID=${1}
if [ -z "$PROJECT_ID" ]
  then
    echo "No project ID supplied."
  else
    echo "Deploying dash demo to project ${PROJECT_ID}"

    gcloud run deploy dash-demo \
    --image=europe-west1-docker.pkg.dev/${PROJECT_ID}/dash-repo/dash-demo:latest \
    --platform=managed \
    --project=${PROJECT_ID} \
    --region=europe-west1 \
    --timeout=60 \
    --concurrency=10 \
    --cpu=1 \
    --max-instances=4 \
    --allow-unauthenticated
fi





