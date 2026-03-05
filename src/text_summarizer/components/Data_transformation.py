import os
from src.text_summarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk

from src.text_summarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config
        self.tokenizer=AutoTokenizer.from_pretrained(config.tokenizerName)

    def convertExamplesTofeatures(self,exampleBatch):
        inputEncoding=self.tokenizer(exampleBatch['dialogue'],max_length=1024, truncation = True) 
       # with self.tokenizer.asTargetTokenizer():
        targetEncoding=self.tokenizer(exampleBatch['summary'],max_length=128, truncation= True)

        return{
                'input_ids': inputEncoding['input_ids'],
                'attention_mask': inputEncoding['attention_mask'],
                'labels': targetEncoding['input_ids']
        }
    def convert(self):
        datasetSamsum=load_from_disk(self.config.dataPath)
        datasetSamsumPt= datasetSamsum.map(self.convertExamplesTofeatures)
        datasetSamsumPt.save_to_disk(os.path.join(self.config.rootDir,"samsumDataset"))
        
                                           
        
