import os
from pathlib import Path
import logging
list_of_files = [
    ".github/workflow/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingection.py",
    "src/components/data_transformation.py",
    "src/components/model.training.py",
    "src/components/model.evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/traning_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logger.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiments.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # crate an empth file
