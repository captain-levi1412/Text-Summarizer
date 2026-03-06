from src.text_summarizer.constants import *
from src.text_summarizer.utils.common import readYaml, createDir
from src.text_summarizer.entity import DataIngestionConfig, DataTransformationConfig, ModelTrainingConfig

class ConfigManager:
    def __init__(self,
                 config_path=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):
        self.config=readYaml(config_path)
        self.params=readYaml(params_filepath)

        createDir([self.config.artifactsRoots])

    def getDataIngestionConfig(self) -> DataIngestionConfig:
        config=self.config.dataIngestion
        createDir([config.rootDir])

        dataIngestionConfig=DataIngestionConfig(
            rootDir= config.rootDir,
            sourceURL=config.sourceURL,
            localDataFile=config.localDataFile,
            unzipDir= config.unzipDir,
            )

        return dataIngestionConfig
    



    def __init__(self,
                 config_path=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):
        self.config=readYaml(config_path)
        self.params=readYaml(params_filepath)

        createDir([self.config.artifactsRoots])

    def getDataTransformationConfig(self)-> DataTransformationConfig:
        config= self.config.dataTransformation
        
        createDir([config.rootDir])
        dataTransformationConfig=DataTransformationConfig(
            rootDir=config.rootDir,
            dataPath=config.dataPath,
            tokenizerName=config.tokenizerName
        )
        return dataTransformationConfig


    def getModelTrainingConfig(self)-> ModelTrainingConfig:
            config= self.config.modelTraining
            params=self.params.TrainingArguments
            
            createDir([config.rootDir])
            modelTrainingConfig=ModelTrainingConfig(
                rootDir=config.rootDir,
                dataPath=config.dataPath,
                modelCkpt=config.modelCkpt,
                numTrainEpoche=params.numTrainEpoche,
                warmupStreps=params.warmupStreps,
                perDeviceTrainBatchSize=params.perDeviceTrainBatchSize,
                weightDecay=params.weightDecay,
                loggingSteps=params.loggingSteps,
                evaluationStratergy=params.evaluationStratergy,
                evalSteps=params.evalSteps,
                saveSteps=params.saveSteps,
                gradientAccumulationSteps=params.gradientAccumulationSteps
                
            )
            return modelTrainingConfig
