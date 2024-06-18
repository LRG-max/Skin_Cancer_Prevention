#########
### DOCKER LOCAL
#########

build_container_local:
	docker build --tag=$$IMAGE:dev .

run_container_local:
	docker run -it -e PORT=8000 -p 8000:8000 $$IMAGE:dev



#########
## DOCKER DEPLOYMENT
#########

# Step 1 ( ONLY FIRST TIME)
allow_docker_push:
	gcloud auth configure-docker $$GCP_REGION-docker.pkg.dev

# Step 2 ( ONLY FIRST TIME)
create_artifacts_repo:
	gcloud artifacts repositories create $$ARTIFACTSREPO --repository-format=docker \
	--location=$$GCP_REGION --description="Repository for storing images"

# Step 3
build_for_production:
	docker build -t  $$GCP_REGION-docker.pkg.dev/$$GCP_PROJECT/$$ARTIFACTSREPO/$$IMAGE:prod .


## Step 4
push_image_production:
	docker push $$GCP_REGION-docker.pkg.dev/$$GCP_PROJECT/$$ARTIFACTSREPO/$$IMAGE:prod

# Step 5 -> will give us an API URL !!!
deploy_to_cloud_run:
	gcloud run deploy --image $$GCP_REGION-docker.pkg.dev/$$GCP_PROJECT/$$ARTIFACTSREPO/$$IMAGE:prod --memory $$MEMORY --region $$GCP_REGION


# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

check_code:
	@flake8 scripts/* Skin_Cancer_Prevention/*.py

black:
	@black scripts/* Skin_Cancer_Prevention/*.py

test:
	@coverage run -m pytest tests/*.py
	@coverage report -m --omit="${VIRTUAL_ENV}/lib/python*"

ftest:
	@Write me

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr Skin_Cancer_Prevention-*.dist-info
	@rm -fr Skin_Cancer_Prevention.egg-info

install:
	@pip install . -U

all: clean install test black check_code

count_lines:
	@find ./ -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./scripts -name '*-*' -exec  wc -l {} \; | sort -n| awk \
		        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./tests -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''

# ----------------------------------
#      UPLOAD PACKAGE TO PYPI
# ----------------------------------
PYPI_USERNAME=<AUTHOR>
build:
	@python setup.py sdist bdist_wheel

pypi_test:
	@twine upload -r testpypi dist/* -u $(PYPI_USERNAME)

pypi:
	@twine upload dist/* -u $(PYPI_USERNAME)
