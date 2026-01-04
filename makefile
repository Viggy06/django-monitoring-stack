.PHONY: setup-docker docker-permission

setup-docker:
	chmod +x setup_docker_script.sh
	./setup_docker_script.sh

up-all:
	@docker compose up -d --build

api-up:
	@docker compose up -d

api-down:
	@docker compose down

api-rebuild:
	@docker compose down && docker compose up -d --build
