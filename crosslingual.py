import numpy as np
import torch
from torch.nn.utils.rnn import pad_sequence
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity

class CrossLanguageCloneDetector:
    def __init__(self, model_name):
        
        self.model = AutoModel.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def generate_embedding(self, code):
        # Tokenize the code
        inputs = tokenizer(code, return_tensors="pt", padding=True, truncation=True)
        # Generate the model's output
        with torch.no_grad():
            outputs = self.model(**inputs)
        # Extract the embedding for the [CLS] token
        embedding = outputs.last_hidden_state[:, 0, :]
        # Normalize the embedding
        embedding = torch.nn.functional.normalize(embedding, p=2, dim=1)
        return embedding

    def get_code_embedding(self, code):
        """
        Generate an embedding for a given piece of code.
        """
        inputs = self.tokenizer(code, return_tensors='pt')
        outputs = self.model(**inputs)
        return outputs.last_hidden_state[0].mean(dim=0).detach().numpy()

    def compute_similarity(self, embedding1, embedding2):
        """
        Compute similarity between two embeddings.
        """
        return cosine_similarity([embedding1], [embedding2])[0][0]

    def detect_clones(self, code1, code2):
        """
        Detect clones between two pieces of code.
        """
        embedding1 = self.get_code_embedding(code1)
        embedding2 = self.get_code_embedding(code2)

        similarity = self.compute_similarity(embedding1, embedding2)
        return similarity

# Initialize the clone detector
model_name = "microsoft/codebert-base"
clone_detector = CrossLanguageCloneDetector(model_name)

# Example 0: Codes in two different languages
code1 = "def add(a, b): return a + b"  # Python
code2 = "int add(int a, int b) { return a + b; }"  # Java

similarity_score = clone_detector.detect_clones(code1, code2)
print(f"Similarity score: {similarity_score}")

# Example 1: Similar codes in two different languages
code1 = "def subtract(a, b): return a - b"  # Python
code2 = "int subtract(int a, int b) { return a - b; }"  # Java

similarity_score = clone_detector.detect_clones(code1, code2)
print(f"Similarity score: {similarity_score}")

# Example 2: Different codes in two different languages
code1 = "def multiply(a, b): return a * b"  # Python
code2 = "int divide(int a, int b) { return a / b; }"  # Java

similarity_score = clone_detector.detect_clones(code1, code2)
print(f"Similarity score: {similarity_score}")

# Example 3: Similar codes in the same language
code1 = "def add(a, b): return a + b"  # Python
code2 = "def sum(a, b): return a + b"  # Python

similarity_score = clone_detector.detect_clones(code1, code2)
print(f"Similarity score: {similarity_score}")
