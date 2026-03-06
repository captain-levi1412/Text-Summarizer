from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    rootDir:Path
    sourceURL:Path
    localDataFile:Path
    unzipDir:Path


@dataclass
class DataTransformationConfig:
    rootDir:Path
    dataPath:Path
    tokenizerName:Path

@dataclass
class ModelTrainingConfig:
    rootDir:Path
    dataPath:Path
    modelCkpt:Path
    numTrainEpoche: int
    warmupStreps: int
    perDeviceTrainBatchSize: int
    weightDecay: float
    loggingSteps: int
    evaluationStratergy: str
    evalSteps: int
    saveSteps: float
    gradientAccumulationSteps: int

@dataclass(frozen=True)
class ModelEvalConfig:
    rootDir:Path
    dataPath:Path
    modelPath:Path
    tokenizerPath: Path
    metricFileName: Path
    