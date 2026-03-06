from src.text_summarizer.config.configuration import ConfigManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config=ConfigManager().getModelEvalConfig()

    def predict(self,text):
        tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizerPath)
        genKwargs={"length_penalty":0.8,"num_beams":8, "max_length":128}
        pipe=pipeline("text-generation", model=self.config.modelPath,tokenizer=tokenizer)

        print("Dialouge:")
        print(text)

        output=pipe(text, **genKwargs)[0]["generated_text"]
        print("\nModel Summary")
        print(output)

        return output
