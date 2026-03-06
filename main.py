from src.text_summarizer.logging  import logger
from src.text_summarizer.pipeline.stage_1_data_ingestion_pipelines import DataIngestionTrainingPipeline
from src.text_summarizer.pipeline.stage_2_data_transformation_pipelines import DataTransformationTrainingPipeline
from src.text_summarizer.pipeline.stage_3_model_training_pipelines import ModelTrainingPipeline
from src.text_summarizer.pipeline.stage_4_model_evaluation_pipelines import ModelEvalPipeline

STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f"stage{STAGE_NAME} initiated")
    dataIngestionPipeline= DataIngestionTrainingPipeline()
    dataIngestionPipeline.initiateDataIngestion()
    logger.info(f"stage{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Transformation stage"

try:
    logger.info(f"stage{STAGE_NAME} initiated")
    dataTransformationPipeline= DataTransformationTrainingPipeline()
    dataTransformationPipeline.initiateDataTransformation()
    logger.info(f"stage{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Model Training stage"

try:
    logger.info(f"stage{STAGE_NAME} initiated")
    modelTrainingPipeline= ModelTrainingPipeline()
    modelTrainingPipeline.initiateModelTraining()
    logger.info(f"stage{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Model Evaluation stage"

try:
    logger.info(f"stage{STAGE_NAME} initiated")
    modelEvalPipeline= ModelEvalPipeline()
    modelEvalPipeline.initiateModelEval()
    logger.info(f"stage{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e