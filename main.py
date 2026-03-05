from src.text_summarizer.logging  import logger
from src.text_summarizer.pipeline.stage_data_ingestion_pipelinr import DataIngestionTrainingPipeline


STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f"stage{STAGE_NAME} initiated")
    dataIngestionPipeline= DataIngestionTrainingPipeline()
    dataIngestionPipeline.initiateDataIngestion()
    logger.info(f"stage{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e