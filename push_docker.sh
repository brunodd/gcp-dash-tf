PROJECT_ID=${1}
if [ -z "$PROJECT_ID" ]
  then
    echo "No project ID supplied."
  else
    echo "Build, tag and push docker image"
    docker build --platform=linux/amd64 --tag europe-west1-docker.pkg.dev/${PROJECT_ID}/dash-repo/dash-demo:latest -t dash-demo .

    echo "Push image to project ${PROJECT_ID}'s artifact registry"
    docker push europe-west1-docker.pkg.dev/${PROJECT_ID}/dash-repo/dash-demo:latest
fi
