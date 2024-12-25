# Makefile
.PHONY: docker-build typing

define IMAGE_NAME
types_annotations
endef


docker-build:
	docker build -t $(IMAGE_NAME) .

typing:
	docker run $(IMAGE_NAME) mypy .
