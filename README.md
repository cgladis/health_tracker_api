# Health Tracker API

## Description
This project is an API for tracking user health data. It calculates a **health score** based on step count, sleep duration, and glucose level.

## 🔧 Installation & Running

### 1️⃣ Running without Docker
#### Requirements:
- Python 3.9+
- `pip` installed

#### Installation & Running:
```bash
# Clone the repository
git clone https://github.com/cgladis/health_tracker_api.git
cd health_tracker_api

# Install dependencies
pip install -r requirements.txt

# Create a `.env` file with necessary environment variables
cp .env.example .env

# Start the server
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
After starting, the API will be available at `http://localhost:8000`

### 2️⃣ Running with Docker
#### Requirements:
- Docker installed

#### Build & Run:
```bash
# Build Docker image
docker build -t health_tracker_api .

# Run the container with environment variables
docker run --env-file .env -p 8000:8000 health_tracker_api
```

## 🚀 API Endpoints
### 1️⃣ Get Health Score
```
GET /api/get_health_score/{user_id}
```
#### Example Request:
```bash
curl -X GET http://localhost:8000/api/get_health_score/1
```
#### Example Response:
```json
{
    "user_id": 1,
    "health_score": 85.4
}
```
#### Query Parameters:
- `user_id` (integer) – ID of the user whose health score should be calculated.

## 🛠 Automation with Makefile
For convenience, you can use `Makefile`:

```makefile
install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

docker-build:
	docker build -t health_tracker_api .

docker-run:
	docker run --env-file .env -p 8000:8000 health_tracker_api
```

Now you can run:
```bash
make install  # Install dependencies
make run      # Start the server
make docker-build  # Build Docker image
make docker-run  # Run the container
```

## ✅ Running Tests
```bash
pytest
```

## 📖 Environment Variables
The API requires some environment variables to be set before running.  
You can create a `.env` file by copying the example:
```bash
cp .env.example .env
```
Then update the variables inside `.env`.

## 📖 Theoretical Questions & Answers
You can find answers to theoretical questions in [THEORY.md](./THEORY.md).

## 📩 Feedback
If you have any questions, feel free to open an issue in [the repository](https://github.com/cgladis/health_tracker_api/issues).

---
**Author:** Sasha
