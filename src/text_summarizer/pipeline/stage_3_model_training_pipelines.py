

from src.text_summarizer.components.Model_Training import ModelTraining
from src.text_summarizer.config.configuration import ConfigManager


class ModelTrainingPipeline:
    def __init__(self):
        pass


    def initiateModelTraining(self):
        config= ConfigManager()
        modelTrainingConfig=config.getModelTrainingConfig()
        modelTraining=ModelTraining(config=modelTrainingConfig)
        modelTraining.train()
