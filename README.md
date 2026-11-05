# Weather service

## Introduction

This tech test is to create a weather service. You can continue from the starter code provided, or start over.

Build the load and API endpoints as described under "What to build" below. The server is a simple Python Flask application. The database in this test is Postgres.

## Time

Plan for **1-2 hours**. The goal of this test is to create a database with the readings loaded, and a working API in front of it. 
Additional thoughts on improvements that cannot be implemented in that time should be noted in a comment, or add a readme with thoughts and comments. 

## Getting started

You need Python 3.14, [uv](https://docs.astral.sh/uv/), and Docker. The commands below are from the `backend-weather-service` directory.

### Database

Postgres runs in Docker. The database starts with no tables. Check the docker compose file to see the database configuration.

```bash
docker compose up -d
```

```text
postgresql://weather:weather@127.0.0.1:5432/weather
```

`db/diffs/0001_initial.sql` is the first database diff. Postgres applies the files in `db/diffs`, in name order, when the data directory is first created. That first diff does not create tables. Further schema changes are yours. Add them as later files in `db/diffs`.


### API

From `backend/`. `uv sync` creates `.venv` and installs the API dependencies.

```bash
cd backend
uv sync
uv run python app.py
```

The API listens on `http://127.0.0.1:5000`.

Check it:

```bash
curl http://127.0.0.1:5000/api/health
```

## The file

`measurements.txt` is UTF-8. It sits in this directory, next to `backend/`.

A usable line looks like this:

```text
Hamburg;2024-01-01T00:00:00Z;3.7
```

The name is the city. The timestamp is UTC. The number is degrees Celsius. Each line is one reading. The readings run from 1 Jan 2024 00:00 UTC through 2 Jan 2024 23:45 UTC.

Every reading is on a 15-minute boundary. The minutes are `00`, `15`, `30`, or `45`, and the seconds are `00`. Some slots have no reading.

This file is a stand in for the usual fetch wich would be for example an api or kafka topic or sqs queue or another source of data.

## What to build

Store the readings in Postgres. The API serves data from that database.

The Compose file is the database setup for this test. You can replace Postgres with another database. If you do, write that choice down.

`GET /api/health` has to keep working.

### Load

Read `measurements.txt` into the database. This should happen when the server starts. 
Data loading should not block the api availability. 

Loading the file again must not store a second copy of a reading that is already there.

A missing 15-minute slot is not a measurement. Statistics below use the readings that were stored.

### API

**Add an endpoint to GET all cities and their statistics**

Temperature statistics for every city in the database. For each city, include the minimum temperature, the maximum temperature, the mean temperature, and the number of measurements. An optional `search` query parameter filters the cities by name.

**Add an endpoint to GET all statistics for a specific city**

The same statistics for one city. If that city is not in the database, return 404.

**Add an endpoint to GET the timeseries temperature data for a specific city**

The temperature timeseries for one city. Accept a start and an end. If neither is given, choose a default range and write it down.

The slots are every 15 minutes from the start through the end. A slot with no stored reading has to be visible in the response. 

**Add an endpoint to trigger a background job to load the data from the file**

The file load is a stand in for a data source. Some notes on considerations on what this would likely also include (auth, dateranges etc.) would be helpful.

**Add an endpoint to manually override a temperature reading for a specific city and timestamp**

Add a way to manually override a temperature reading. Note that this should be trackable and auditable. 
This endpoint has a vague design, so note your assumptions and design choices.


## What to submit

Submission as a git branch or a email with zip of the files are fine. Include the code, the note about the choices above, and the run instructions.

## If something is unclear

Pick a reasonable rule/assumption, implement it, and write it down. That note is part of the submission.
