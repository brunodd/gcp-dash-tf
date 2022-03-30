provider "google" {}

resource "google_project" "my-demo" {
	name = "my-demo-project"
	project_id = "my-demo-project-asdfsd"  # TODO: rename project_id (between 6 and 30 chars)
}
