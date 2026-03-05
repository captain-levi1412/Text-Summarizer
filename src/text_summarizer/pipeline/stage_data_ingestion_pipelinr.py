from src.text_summarizer.components.Data_ingestion import DataIngestion
from src.text_summarizer.config.configuration import ConfigManager




class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiateDataIngestion(self):
        config=ConfigManager()
        dataIngestionConfig=config.getDataIngestionConfig()
        dataIngestion=DataIngestion(config=dataIngestionConfig)

        dataIngestion.downloadFile()
        dataIngestion.extractZipFile()

    
    