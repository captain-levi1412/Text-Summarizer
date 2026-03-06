# Text‑Summarizer

This repository contains a simple pipeline‑based Python project that
downloads/ingests text data, transforms it, trains a summarization model
and finally evaluates it.  Each step of the workflow is implemented as a
“stage” and orchestrated from a single `main.py` script.

---

## Project overview

The stages executed by `main.py` are:

1. **Data ingestion** – fetch raw text (from disk, web, etc.) and write it
   to a standard location.
2. **Data transformation** – clean, tokenize and vectorise the raw text so
   that it can be passed to a model.
3. **Model training** – build and fit a summarization model (e.g. seq2seq,
   transformer) using the transformed data.
4. **Model evaluation** – score the trained model on a hold‑out set and
   produce metrics/reports.

Each stage has its own pipeline class under `src/text_summarizer/pipeline`
and logs its progress using the shared logger.

The pipeline classes live in:

* `src/text_summarizer/pipeline/ingestion.py` – data ingestion
* `src/text_summarizer/pipeline/transformation.py` – data transformation
* `src/text_summarizer/pipeline/training.py` – model training
* `src/text_summarizer/pipeline/evaluation.py` – model evaluation

Additional utility code (e.g. for configuration, exceptions,
constants) is under `src/text_summarizer` with a simple logger in
`src/text_summarizer/logging.py`.

`main.py` is the entry point; it constructs and runs each stage in turn,
wrapping every step in a `try/except` block so that failures are logged and
re‑raised.

---

## Getting started

### Prerequisites

* Python 3.9+ (the project was developed on Windows 10/11 but is
  cross‑platform).
* [pipenv](https://pipenv.pypa.io/) or [venv](https://docs.python.org/3/library/venv.html)
  for a virtual environment.
* Internet access if data ingestion pulls from a remote source.

### Installation

1. **Clone the repository:**

```bash
   git clone https://github.com/your‑username/Text-Summarizer.git
   cd "Text-Summarizer"
```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
.\venv\Scripts\activate    # Windows
# or on macOS/Linux: source venv/bin/activate
```

3. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

Note: If the project uses additional packages (e.g. `scikit-learn`,
`pandas`, `torch`), add them to [requirements.txt](requirements.txt).

**Running the pipeline**
Execute the main script from the project root:
```bash
python main.py
```

Logs are emitted to the console (and optionally to a file configured in
[src/text_summarizer/logging.py](src/text_summarizer/logging.py)). Each stage logs its start/completion and
any exceptions encountered.

If you need to run an individual stage for development, import and call
its pipeline class directly in a Python shell or a new script.

## Project Structure
```text
Text-Summarizer/
│
├── README.md                   # this file
├── main.py                     # pipeline orchestrator
├── requirements.txt            # dependency list
└── src/
    └── text_summarizer/
        ├── __init__.py
        ├── logging.py          # configured logger instance
        ├── config/             # optional configuration helpers
        ├── constants.py        # file paths, hyper‑parameters, etc.
        ├── exceptions.py       # custom exception types
        └── pipeline/
            ├── stage_1_data_ingestion_pipelines.py
            ├── stage_2_data_transformation_pipelines.py
            ├── stage_3_model_training_pipelines.py
            └── stage_4_model_evaluation_pipelines.py
```
Add new modules or stages under [text_summarizer](src/text_summarizer) as the project
expands.

### Development
- **Logging** – the logger object is imported from
src/text_summarizer/logging.py. Adjust formatting/handlers there.

- **Configuration** – store paths and hyper‑parameters in a central
config file or use environment variables.

- **Testing** – add unit tests under a `tests/` folder and run them with
`pytest:`

Example test for a pipeline method:

``` bash
def test_data_transformation(tmp_path):
    pipeline = DataTransformationTrainingPipeline(...)
    # prepare dummy input, call pipeline.initiateDataTransformation()
    # assert expected output files exist
```

### Extending the project

1. **Additional data sources** – extend the ingestion pipeline or add new
stage modules.
2. **Model variants** – encapsulate different algorithms behind a common
interface (ModelTrainingPipeline could accept a strategy object).
3. **Deployment** – wrap the trained model in an API (Flask/FastAPI) and
serve summaries.

### Contributing
1. Fork the repo.
2. Create a feature branch:`git checkout -b feature/my-feature.`
3. Commit your changes and open a pull request.
4. Ensure new code is covered by tests and that the pipeline still runs.

## License
Specify the licence under which you are releasing the code (e.g. MIT).


