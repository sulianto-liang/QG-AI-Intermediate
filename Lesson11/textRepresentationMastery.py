import math
import numpy as np
from collections import Counter
import gensim.downloader as api
import gensim.models as Word2Vec
import re
import warnings
warnings.filterwarnings('ignore')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import itertools


class TFIDFCalculator:
    def __init__(self):
        self.vocabulary = set()
        self.documents = []

    def preprocess_text(self, text):
        text = re.sub(r'[^\w\s]', '', text.lower())
        return text.split()

    def add_documents(self, documents):
        self.documents=[]
        for doc in documents:
            tokens = self.preprocess_text(doc)
            self.documents.append(tokens)
            self.vocabulary.update(tokens)

        print(f"Added {len(self.documents)} documents to corpus")
        print(f"Vocabulary size: {len(self.vocabulary)}")

    def calculate_tf(self, document, term):
        term_count = document.count(term)
        total_terms = len(document)
        tf = term_count / total_terms if total_terms > 0 else 0

        #print(f"  TF (''{term}'): {term_count}/{total_terms} = {tf:.4f})")
        return tf

    def calculate_idf(self, term):
        doc_containing_term = sum(1 for doc in self.documents if term in doc)
        total_docs = len(self.documents)
        idf = math.log(total_docs / doc_containing_term) if doc_containing_term > 0 else 0

        #print(f"  IDF ('{term}'): log({total_docs}/{doc_containing_term}) = {idf:.4f}")
        return idf

    def calculate_tfidf(self, doc_index, term):
        if doc_index >= len(self.documents):
            return 0

        document = self.documents[doc_index]

        #print(f"\n Calculating TF-IDF for '{term}' in Document {doc_index+1}")
        tf = self.calculate_tf(document, term)
        idf = self.calculate_idf(term)

        tfidf = tf * idf

        #print(f"TF-IDF ('{term}'): {tf:.4f} * {idf:.4f} = {tfidf:.4f}")
        return tfidf

    def get_tfidf_vector(self, doc_index):
        if doc_index >= len(self.documents):
            return {}
        vector = {}
        for term in self.vocabulary:
            vector[term] = self.calculate_tfidf(doc_index, term)

        return

    def find_most_important_words(self, doc_index, top_n=5):
        tfidf={}
        for term in self.vocabulary:
            tfidf[term]=self.calculate_tfidf(doc_index, term)

        sorted_tfidf_desc = dict(sorted(tfidf.items(), key=lambda item: item[1], reverse=True))

        print(f"\nTop 5 word with highest TF-IDF in Document {doc_index+1} : {dict(itertools.islice(sorted_tfidf_desc.items(), top_n))}")

    def compare_documents(doc1_index, doc2_index):
        pass

def tf_idf():
    print("=" * 60)
    print("🔢 TF-IDF DEEP DIVE")
    print("=" * 60)

    # Sample documents
    documents = [
        "This movie is absolutely fantastic and amazing",
        "The movie was terrible and boring",
        "Amazing acting but terrible plot",
        "Fantastic movie with great acting"
    ]

    print("📄 Movie Review Documents:")
    for i, doc in enumerate(documents):
        print(f"  Doc {i + 1}: \"{doc}\"")

    tfidf_calc = TFIDFCalculator()
    tfidf_calc.add_documents(documents)

    print("\n" + "=" * 40)
    print("MANUAL TF-IDF CALCULATION")
    print("=" * 40)

    print("\n1. Calculate the TF - IDF score for the word 'amazing' in Document 1")
    tfidf_calc.calculate_tfidf(0, "amazing")

    print("\n2. Calculate the TF - IDF score for the word 'terrible' in Document 2")
    tfidf_calc.calculate_tfidf(1, "terrible")

    print("\n" + "=" * 40)
    print("SKLEARN TF-IDF COMPARISON")
    print("=" * 40)

    original_docs = [" ".join(doc) for doc in tfidf_calc.documents]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(original_docs)
    feature_names = vectorizer.get_feature_names_out()

    print("3. Show all intermediate steps (TF and IDF calculations)")

    print(f"📊 TF-IDF Matrix shape: {tfidf_matrix.shape}")
    print(f"🔤 Features: {list(feature_names)}")

    for j, dc in enumerate(documents):
        print(f"\n📋 TF-IDF scores for Document {j+1}:")
        doc_tfidf = tfidf_matrix[j].toarray()[0]
        for i, score in enumerate(doc_tfidf):
            if score > 0:
                print(f"  {feature_names[i]}: {score:.4f}")

    for j, dc in enumerate(documents):
        tfidf_calc.find_most_important_words(j,5)

def main():
    tf_idf()

if __name__ == "__main__":
    main()