import torch
from transformers import BertTokenizer, BertModel
from neuro_chain_hub import NeuroChainEdgeNLP

class NeuroChainEdgeNLP:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')

    def process_text(self, text):
        # Tokenize input text
        inputs = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=512,
            return_attention_mask=True,
            return_tensors='pt'
        )

        # Run BERT model
        outputs = self.model(inputs['input_ids'], attention_mask=inputs['attention_mask'])
        last_hidden_state = outputs.last_hidden_state

        # Get sentiment analysis output
        sentiment_output = torch.nn.functional.softmax(last_hidden_state[:, 0, :], dim=1)
        return sentiment_output

nlp = NeuroChainEdgeNLP()
text = "This is a sample text."
sentiment_output = nlp.process_text(text)
print(sentiment_output)
