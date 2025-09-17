# MLOps Assignment 4: Automating ML Pipelines with CI/CD (GitHub Actions + DVC)

## Objective

This project demonstrates the automation of a machine learning pipeline using a CI/CD workflow with GitHub Actions and Data Version Control (DVC). The pipeline is designed to automatically train and evaluate a model whenever there are changes to the code or parameters.

## Pipeline Overview

The project uses DVC to manage the machine learning pipeline, defining the following stages in `dvc.yaml`:

1.  **`train`**: Trains a simple linear regression model using data from `data/data.csv` and saves the model to `model.pkl`. It tracks hyperparameters from `params.yaml`.
2.  **`evaluate`**: Loads the trained model, makes predictions, and calculates performance metrics. The metrics are saved to `metrics.json`.

The CI/CD workflow, defined in `.github/workflows/ci.yaml`, automates this process:

* It is triggered by `push` and `pull_request` events to the `main` branch.
* It sets up a Python environment and installs all dependencies listed in `requirements.txt`.
* It runs `dvc repro`, which automatically re-executes the pipeline if any of the dependencies (code, data, or parameters) have changed.
* Finally, it runs `dvc metrics show` to display the final model performance metrics in the workflow logs.

## Project Structure

.
├── .github/workflows/
│   └── ci.yaml               # GitHub Actions CI/CD workflow
├── data/
│   └── data.csv              # Input data file
├── src/
│   ├── evaluate.py           # Model evaluation script
│   └── train.py              # Model training script
├── dvc.yaml                  # DVC pipeline definition
├── params.yaml               # Model hyperparameters
├── requirements.txt          # Python dependencies
└── README.md                 # Project README file

## How to Run Locally

1.  **Clone the repository and navigate to the project directory:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Reproduce the pipeline using DVC:**
    ```bash
    dvc repro
    ```

4.  **View the metrics:**
    ```bash
    dvc metrics show
    ```

## Reliability of CI/CD vs. Local Runs

Running a CI/CD pipeline on a separate runner is significantly more reliable than a local run. It ensures consistency by providing a clean, standardized environment, which eliminates "it works on my machine" issues. This process validates that the code, dependencies, and data pipeline are robust and reproducible, independent of any local configurations or pre-existing files.
