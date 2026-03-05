from src.text_summarizer.components.Data_transformation import DataTransformation
from src.text_summarizer.config.configuration import ConfigManager


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiateDataTransformation(self):

        config=ConfigManager()
        dataTransformationConfig=config.getDataTransformationConfig()
        dataTrandformation=DataTransformation(config=dataTransformationConfig)
        dataTrandformation.convert()