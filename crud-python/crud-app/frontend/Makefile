IMAGE = crud-fe
TAG = v2

build:
	docker build -t $(IMAGE):$(TAG) .


build-version:
	docker build -t $(IMAGE):$(version) .
load:
	docker load < $(IMAGE)-$(TAG).tar

run:
	docker run -p 3000:3000 $(IMAGE):$(TAG)

push:
	docker push $(IMAGE):$(TAG)

clean:
	docker rmi $(IMAGE):$(TAG)
deploy:
	docker compose up
undeploy:
	docker compose down