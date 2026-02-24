# Viral Artists Pipeline

A data pipeline that tracks viral artists using Last.fm API, Docker, and AWS S3.

## Tech Stack
- **Python** - Data fetching & processing
- **Last.fm API** - Real-time artist data
- **Docker** - Containerization
- **AWS S3** - Cloud data storage

## What It Does
1. Fetches Top 50 viral artists from Last.fm Chart
2. Collects listeners count, playcount, and tags
3. Uploads structured JSON data to AWS S3

## How To Run
1. Clone the repo
2. Create `.env` file with your API keys
3. Run with Docker:
```bash
docker-compose run pipeline

Project Structure
├── src/
│   ├── lastfm_client.py   # Last.fm API client
│   └── pipeline.py        # Main pipeline
├── Dockerfile
├── docker-compose.yml
└── requirements.txt