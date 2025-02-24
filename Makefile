install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

docker-build:
	docker build -t health_tracker_api .

docker-run:
	docker run -p 8000:8000 health_tracker_api
