init:
	@python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install -r requirements.txt && deactivate
run:
	@. .venv/bin/activate && python3 -m app && deactivate