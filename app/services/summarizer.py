from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from ..utils.logger import logger
import re

class Summarizer:
    def __init__(self):
        model_name = "facebook/bart-large-cnn"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.summarizer = pipeline("summarization", model=self.model, tokenizer=self.tokenizer)

    def extractive_summarize(self, text, num_sentences=10):
        sentences = text.split('. ')
        vectorizer = TfidfVectorizer().fit_transform(sentences)
        vectors = vectorizer.toarray()
        
        # Calculate the similarity between all sentences
        sim_matrix = cosine_similarity(vectors)
        
        # Calculate sentence scores
        scores = np.sum(sim_matrix, axis=1)
        
        # Sort sentences by score and select top ones
        ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
        return '. '.join([ranked_sentences[i][1] for i in range(min(num_sentences, len(ranked_sentences)))])

    def summarize(self, text: str, max_length: int = 1024) -> str:
        # First, apply extractive summarization
        extracted_text = self.extractive_summarize(text)
        
        # Then, apply abstractive summarization
        inputs = self.tokenizer([extracted_text], max_length=1024, return_tensors="pt", truncation=True)
        summary_ids = self.model.generate(inputs["input_ids"], num_beams=4, min_length=max_length-100, max_length=max_length, length_penalty=2.0, no_repeat_ngram_size=3)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        # Post-process the summary
        summary = self.post_process_summary(summary)
        
        logger.info(f"Generated summary with {len(summary.split())} words")
        return summary

    def post_process_summary(self, summary):
        # Ensure the summary starts with a capital letter and ends with a period
        summary = summary.capitalize()
        if not summary.endswith('.'):
            summary += '.'
        
        # Remove any incomplete sentences at the end
        last_period = summary.rfind('.')
        if last_period != -1:
            summary = summary[:last_period+1]
        
        # Remove irrelevant details
        summary = re.sub(r'for more information.*?\. ', '', summary, flags=re.IGNORECASE)
        summary = re.sub(r'visit.*?\. ', '', summary, flags=re.IGNORECASE)
        summary = re.sub(r'click here.*?\. ', '', summary, flags=re.IGNORECASE)
        
        return summary
