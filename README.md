
# Like Counter Django Project

This project is a Django-based application that handles batch processing of like counts on posts using Kafka for messaging, Zookeeper for Kafka coordination, and Locust for load testing. The system includes both a Kafka producer and consumer for processing like events.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
5. [Running the Project](#running-the-project)
6. [Testing with Locust](#testing-with-locust)
7. [Project Structure](#project-structure)
8. [Configuration](#configuration)
9. [Contributing](#contributing)
10. [License](#license)

## Project Overview

The Like Counter project allows users to "like" posts, with these events being sent to a Kafka message queue. The events are then processed in batches using a Kafka consumer to update the like count for each post. This approach ensures efficient batch processing and scalability for large volumes of events.

## Features

- **Kafka Producer**: Sends "like" events to a Kafka topic.
- **Kafka Consumer**: Consumes "like" events in batches and updates the like counts in the database.
- **Batch Processing**: Efficiently processes a large number of like events.
- **Load Testing with Locust**: Simulates user interactions and tests the system's performance under high load.
- **Zookeeper**: Used for Kafka coordination.

## Technologies Used

- **Django**: The main web framework for this project.
- **Kafka**: Message broker for producing and consuming like events.
- **Zookeeper**: Service for managing Kafka coordination.
- **Locust**: Load testing tool for simulating user interactions.
- **Docker** : For containerizing the services (Django, Kafka, Zookeeper).

## Setup Instructions

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Django
- Apache Kafka
- Zookeeper
- Locust
- PostgreSQL/MySQL (if using a relational database)
- Docker (optional)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/like-counter-django.git
cd like-counter-django
```

### Step 2: Install Dependencies

Create a virtual environment and install the required Python packages:

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Start Zookeeper and Kafka

Start Zookeeper and Kafka either using Docker or locally installed services.

#### Using Docker

```bash
docker-compose up -d
```

#### Manually

1. Start Zookeeper:

   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
   ```

2. Start Kafka:

   ```bash
   bin/kafka-server-start.sh config/server.properties
   ```

### Step 4: Configure Django Settings

Update your `settings.py` file to configure the database, Kafka server, and other project settings.

### Step 5: Apply Migrations and Run Django Server

```bash
python manage.py migrate
python manage.py runserver
```

## Running the Project

### Step 1: Start the Kafka Producer

The producer will send "like" events to the Kafka topic.



### Step 2: Start the Kafka Consumer

The consumer will read events from the Kafka topic and batch process them.

```bash
python manage.py kafka_consumer
```

## Testing with Locust

Locust is used to simulate user activity and test the system's performance under load.

1. Start the Locust server:

   ```bash
   locust 
   ```

2. Access the Locust web interface at `http://localhost:8089` and configure the number of users and spawn rate.

3. Start the test to simulate "like" events being sent to the Kafka producer.

## Project Structure

```
like-counter/
├── likes/          # Main Django app
│   ├── management/        # Custom management commands for Kafka producer/consumer
│   ├── models.py          # Database models for posts and likes
│   ├── views.py           # Django views (if applicable)
│   ├── kafka_producer.py  # kafka producer 
├── locustfile.py          # Locust configuration for load testing
├── requirements.txt       # Python dependencies
├── manage.py              # Django management script
└── docker-compose.yml     # Docker Compose configuration
```

## Configuration

The project requires some configurations for Kafka and Django settings. These can be defined in the `settings.py` file or as environment variables:

- `KAFKA_BROKER_URL`: Kafka broker URL (e.g., `localhost:9092`).
- `KAFKA_TOPIC`: Kafka topic name for like events.
- `DATABASE`: Database settings for Django.

## Contributing

Contributions are welcome! Please create a pull request with detailed information about the changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

