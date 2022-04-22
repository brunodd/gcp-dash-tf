output "project-id" {
  value = google_project.my-demo.project_id
}

output "artifact-registry-location" {
  value = "${google_artifact_registry_repository.repository.location}-docker.pkg.dev/${google_project.my-demo.project_id}/${google_artifact_registry_repository.repository.repository_id}/"
}