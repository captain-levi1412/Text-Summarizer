from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import  TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
import torch,os
from datasets import load_from_disk

from src.text_summarizer.entity import ModelTrainingConfig

class ModelTraining:
    def __init__(self, config:ModelTrainingConfig):
        self.config= config
    
    def train(self):
        device="cuda" if torch.cuda.is_available() else "cpu"
        tokenizer=AutoTokenizer.from_pretrained(self.config.modelCkpt)
        modelPegasus=AutoModelForSeq2SeqLM.from_pretrained(self.config.modelCkpt)
        seq2seqDataCollator= DataCollatorForSeq2Seq(tokenizer,model=modelPegasus)

        #load data
        datasetSamsumPt=load_from_disk(self.config.dataPath)

        trainingArgs=TrainingArguments(
            output_dir= self.config.rootDir, num_train_epochs= 1, warmup_steps=500,
            per_device_train_batch_size= 1, per_device_eval_batch_size= 1,
            weight_decay=0.01, logging_steps=10,
            eval_steps=500, save_steps=1e6,
            gradient_accumulation_steps=16
            
        )

        trainer= Trainer(model=modelPegasus, args=trainingArgs,
                         processing_class=tokenizer,data_collator=seq2seqDataCollator,
                         train_dataset=datasetSamsumPt["test"],
                         eval_dataset=datasetSamsumPt["validation"])
        trainer.train()

        #save model
        modelPegasus.save_pretrained(os.path.join(self.config.rootDir,"pegasus-samsum-model"))
        ##Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.rootDir,"tokenizer"))