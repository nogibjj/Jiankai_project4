install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest  --nbval-lax *.ipynb
	python -m pytest -vv --cov=hello --cov=cli test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C *.py

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 862353130922.dkr.ecr.us-east-1.amazonaws.com
	docker build -t jiankaiids706project4 .
	docker tag jiankaiids706project4 862353130922.dkr.ecr.us-east-1.amazonaws.com/jiankaiids706project4
	docker push 862353130922.dkr.ecr.us-east-1.amazonaws.com/jiankaiids706project4

all: install format lint test deploy