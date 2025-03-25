# Fraud Detection

## Overview
This project is a fraud detection system that uses a Random Forest machine learning model to calculate the probability of a transaction being fraud or legitimate. The system is designed with a REST API to allow a real time evaluation of the transactions. It also includes real-time alerting via Slack and persistent fraud data logging into a PostgreSQL database.

## Project structure
```
├── app/
│   ├── api/                 # API endpoints
│   │   ├── v1/              # Main API version
│   │   │   ├── views.py     # Handles fraud prediction requests
│   │   │   ├── serializers.py # Data validation
│   │   ├── meta/              # Main API version
│   │   │   ├── views.py     # Handles health requests
│   ├── config/              # Configuration files
│   ├── core/                # Core logic (encoding, handling)
│   ├── assets/              # Stored ML model (model.gz)
├── docker/
│   ├── local/
│   │   ├── Dockerfile       # Docker container setup
│   │   ├── docker-compose.yml # Defines services
├── Notebook.ipynb           # Data analysis and model training
├── requirements.txt         # Python dependencies
├── main.py                  # Entry point for API
├── migrate.py               # Database migration script
├── .env.example             # Environment variable example file
└── README.md                # Documentation
```

## Installation & Setup
### 1. Clone the Repository
```sh
git clone https://github.com/jsbarbosa/cobre.git
cd cobre
```

### 2. Setup Environment Variables
Copy the `.env.example` file and update it with necessary credentials:
```sh
cp .env.example .env
```

## Running the Application
### 1. Build and Run the Docker Container
```sh
docker-compose -f docker/local/docker-compose.yml up --build
```

### 2. Access the API
Once the container is running, the API should be available at:
```
http://0.0.0.0:8001/
```

Go to `http://0.0.0.0:8001/docs` to use the Swagger documentation

## API Endpoints
| Method | Endpoint               | Description                        |
| ------ | ---------------------- | ---------------------------------- |
| POST   | `/api/v1/evaluate`     | Predicts if a transaction is fraud |
| POST   | `/api/v1/notify/slack` | Sends a fraud alert to Slack       |
| GET    | `/api/v1/health`       | Checks API health status           |
| GET    | `/api/v1/version`      | Returns the version of the service |

## Data storage
Every time the `/api/v1/evaluate` endpoint is called:
- The transaction details are stored in a PostgreSQL table called fraud_details.
- The transaction_id serves as the primary index.
- The table stores:
    - Raw data: Date-related and categorical transaction details.
    - Fraud score: The predicted probability of fraud.
    - Processed features: Transformed variables used in the model.
    - Timestamps:
        - `created_at`: When the record was inserted.
        - `updated_at`: When the record was last modified.
        - `deleted_at`: Supports soft deletes for data integrity.
