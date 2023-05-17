# ENV_KUBE_NAMESPACE ?= oms

# dockerized-test-bifrost:
# 	mkdir -p test_reports
# 	docker-compose -f docker-compose-test.yml build --force-rm --parallel --build-arg ENV=test
# 	docker-compose -f docker-compose-test.yml run -e ENV=test db_migrations
# 	docker-compose -f docker-compose-test.yml run -e ENV=test bifrost_tests

# dockerized-tests: dockerized-test-bifrost
# 	echo "Running tests in docker containers"

# dockerized-app:
# 	docker-compose -f docker-compose-test.yml run -e ENV=test bifrost_app python manage.py migrate
# 	docker-compose -f docker-compose-test.yml run -d -e ENV=test bifrost_app python manage.py runserver

non_container_dev:
	docker-compose -f dev/non_containerized/datastores.yaml up

# kube_deploy:
# 	skaffold run -n ${ENV_KUBE_NAMESPACE}

docker-code-lint:
	echo "Checking Codestyle"
	docker run --rm -v ${CURDIR}:/data cytopia/black --check .
