# Bikeshare Demand Forecast

This project forecasts short-term bike-share demand: the number of trips
starting at a given station in a given hour, predicted one day ahead. The
data comes from the [Capital Bikeshare trip history archive](https://s3.amazonaws.com/capitalbikeshare-data/index.html),
the monthly trip data that Capital Bikeshare (Washington, DC) publishes
publicly.

## How it's built

The system is built in four stages, each one working end to end before the
next begins:

1. **Pipeline spine** — the project skeleton, configuration, and entry point
   that every later stage plugs into.
2. **Data layer** — downloading the monthly trip archives and turning them
   into a station-hour panel ready for modelling.
3. **Serving** — a baseline and a learned model, evaluated on a temporal
   split, with a way to produce forecasts.
4. **Retraining and monitoring** — keeping the model current as new months
   of data are published, and watching for drift.

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
