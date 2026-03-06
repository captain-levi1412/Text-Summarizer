from src.text_summarizer.config.configuration import ConfigManager
from src.text_summarizer.components.Model_Evaluation import ModelEval


class ModelEvalPipeline:
    def __init__(self):
        pass

    def initiateModelEval(self):
        config = ConfigManager()
        modelEvalConfig = config.getModelEvalConfig()
        modelEvalutaion= ModelEval(config=modelEvalConfig)
        modelEvalutaion.evaluate()