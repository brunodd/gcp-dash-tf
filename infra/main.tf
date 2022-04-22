provider "google" {}
provider "google-beta" {}

resource "google_project" "my-demo" {
  name            = "my-demo-project"
  project_id      = "my-demo-project-yuhijk"
  billing_account = "01F2B2-FC6127-690B1D"
}

resource "google_project_service" "artifact-service" {
  project                    = google_project.my-demo.project_id
  service                    = "artifactregistry.googleapis.com"
  disable_dependent_services = true
}

resource "google_project_service" "container-service" {
  project                    = google_project.my-demo.project_id
  service                    = "containerregistry.googleapis.com"
  disable_dependent_services = true
}
resource "google_project_service" "cloud-run-service" {
  project                    = google_project.my-demo.project_id
  service                    = "run.googleapis.com"
  disable_dependent_services = true
}

resource "google_artifact_registry_repository" "repository" {
  provider = google-beta

  location      = "europe-west1"
  project       = google_project.my-demo.project_id
  format        = "DOCKER"
  repository_id = "dash-repo"
  depends_on    = [google_project_service.artifact-service]
}
