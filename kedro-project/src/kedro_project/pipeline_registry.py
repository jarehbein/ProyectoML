"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro_project.pipelines.fetch_api import pipeline as fetch_api
from kedro_project.pipelines.business_understanding import pipeline as business_understanding
from kedro_project.pipelines.classification import pipeline as classification_pipeline
from kedro.pipeline import Pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["__default__"] = fetch_api.create_pipeline() + business_understanding.create_pipeline()
    pipelines["fetch_api"] = fetch_api.create_pipeline()
    pipelines["business_understanding"] = business_understanding.create_pipeline()
    pipelines["classification"] = classification_pipeline.create_pipeline()
    return pipelines
