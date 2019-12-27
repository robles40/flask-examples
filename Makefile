
EXAMPLE?=001-hello-world
PORT?=8080

.PHONY: run

run:
	@FLASK_APP=$(EXAMPLE)/app.py FLASK_DEBUG=1 flask run -p $(PORT)
