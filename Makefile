PROJECT_NAME = ${notdir ${PWD}}
PROJECT_NAME := ${shell echo ${PROJECT_NAME} | tr A-Z a-z}
help:
	@echo ":D"
init:
	@python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install -r requirements.txt && deactivate
run:
	@. .venv/bin/activate && python3 -m app && deactivate
build:
	@docker build . -t ${PROJECT_NAME}