# Bikeshare Demand Forecast

This project forecasts short-term bike-share demand: the number of trips
starting at a given station in a given hour, predicted one day ahead. The
data comes from the [Capital Bikeshare trip history archive](https://s3.amazonaws.com/capitalbikeshare-data/index.html),
the monthly trip data that Capital Bikeshare (Washington, DC) publishes
publicly.

## How it's built

The system is built in four stages, each one working end to end before the
next begins:

1. **Pipeline spine**: ingesting a month of trips, splitting it by time,
   scoring a naive baseline against one model, all covered by tests.
2. **Data layer**: trips stored in a database, features built in SQL, and
   experiments tracked so results can be compared.
3. **Serving**: a prediction API over versioned model artifacts, packaged in
   a container and built by CI.
4. **Retraining and monitoring**: retraining as each new month is published,
   comparing against the deployed model, and watching for drift.

## Installing and running

From the repository root, in a WSL2 (Ubuntu) shell:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python run.py check
```

`run.py check` verifies the environment and makes sure the data and results
directories exist.

## Status

Stage 1 is in progress. What currently works: the project skeleton, the
configuration file, the `run.py check` command, and the test suite.
