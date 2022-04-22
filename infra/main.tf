provider "google" {}
provider "google-beta" {}

resource "random_string" "project-suffix" {
  length  = 4
  special = false
  upper   = false
}

locals {
  project_id = "${var.project-name }-${random_string.project-suffix.result}"
}

resource "google_project" "my-demo" {
  name            = var.project-name
  project_id      = local.project_id
  billing_account = var.billing-account
}

resource "google_project_service" "activate-services" {
  for_each = toset([
    "artifactregistry.googleapis.com",
    "containerregistry.googleapis.com",
    "run.googleapis.com"
  ])
  project                    = google_project.my-demo.project_id
  service                    = each.key
  disable_dependent_services = true
}

resource "google_artifact_registry_repository" "repository" {
  provider = google-beta

  location      = "europe-west1"
  project       = google_project.my-demo.project_id
  format        = "DOCKER"
  repository_id = "dash-repo"
  depends_on    = [google_project_service.activate-services]
}
