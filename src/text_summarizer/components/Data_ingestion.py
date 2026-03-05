import os
import urllib.request as request
import zipfile

from src.text_summarizer.logging import logger
from src.text_summarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def downloadFile(self):
        if not os.path.exists(self.config.localDataFile):
            filename, headers= request.urlretrieve(
                url = self.config.sourceURL,
                filename= self.config.localDataFile 
            )
            logger.info(f"file already downloaded")
        else:
            logger.info(f"file already exits")
    
    def extractZipFile(self):
        unzipPath=self.config.unzipDir
        os.makedirs(unzipPath, exist_ok=True)
        with zipfile.ZipFile(self.config.localDataFile,'r') as zipRef:
            zipRef.extractall(unzipPath)
            
