import re
import nltk
import spacy
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter

# Sample social media post
sample_posts = [
    "Just launched our new #AI product! 🚀 Thanks to @team_awesome for the hard work. Check it out: https://oursite.com/product #innovation #tech",

    "Beautiful sunset in San Francisco today 🌅 #photography #california #nature Love this city! @visit_sf",

    "Breaking: Apple announces new iPhone with 50% better battery life! Stock up 12% 📈 #Apple #iPhone #tech #stocks",

    "Feeling grateful for 10,000 followers! 🙏 You all are amazing. Special thanks to @mentor_john for the guidance #milestone #grateful"
]

print("=" * 50)
print("SOCIAL MEDIA POST ANALYSIS")
print("=" * 50)


# 1. REGEX EXTRACTION
print("\n1. REGEX EXTRACTION:")
hashtags=[]
mentions=[]
URLs=[]
numbers=[]
percentages=[]

for item in sample_posts:
    hashtags.extend(re.findall(r'#[^\s]+', item))
    mentions.extend(re.findall(r'@[^\s]+', item))
    URLs.extend(re.findall(r'http[^\s]+', item))
    numbers.extend(re.findall(r'\d+(?:,\d{3})*', item))
    percentages.extend(re.findall(r'\d+(?:\.\d+)?%', item))

print(f"Hashtags:: {hashtags}")
print(f"Mentions: {mentions}")
print(f"URLs:: {URLs}")
print(f"Numbers: {numbers}")
print(f"Percentages: {percentages}")

# 2. NLTK: Analyze sentiment
print("=" * 50)
print("\n2. SENTIMENT ANALYSIS (using NLTK):")
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))
sentiment_analyzer = SentimentIntensityAnalyzer()

for text in sample_posts:
    print(f"\n  • Text: {text}")
    # Tokenization
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    print(f"  • Sentences: {len(sentences)}")
    print(f"  • Words: {len(words)}")

    # Remove punctuation and convert to lowercase
    words_clean = [w.lower() for w in words if w.isalpha()]

    # Remove stop words
    words_filtered = [w for w in words_clean if w not in stop_words]

    print(f"  • Words after cleaning: {len(words_filtered)}")

    # Stemming
    words_stemmed = [stemmer.stem(w) for w in words_filtered]

    # Most common words
    word_freq = Counter(words_stemmed)
    common_words = word_freq.most_common(5)
    print(f"  • Most common words: {[f'{word}({count})' for word, count in common_words]}")

    # Part-of-speech tagging
    pos_tags = nltk.pos_tag(words[:20])  # First 20 words for brevity
    print(f"  • Sample POS tags: {pos_tags[:5]}")

    # Sentiment analysis
    sentiment_scores = sentiment_analyzer.polarity_scores(text)
    #sentiment = max(sentiment_scores, key=sentiment_scores.get)
    #print(f"  • Sentiment: {sentiment.upper()} (score: {sentiment_scores[sentiment]:.2f})")
    print(f"  • Sentiment: ")
    print(f"    - Positive: {sentiment_scores['pos']:.2f}")
    print(f"    - Negative: {sentiment_scores['neg']:.2f}")
    print(f"    - Overall: {'POSITIVE' if sentiment_scores['compound'] > 0.1 else 'NEGATIVE' if sentiment_scores['compound'] < -0.1 else 'NEUTRAL'}")

# 3. SPACY: Find important entities
print("\n3. IMPORTANT ENTITIES (using SpaCy):")
# Initialize SpaCy
try:
    nlp = spacy.load("en_core_web_sm")
    print("✅ SpaCy model loaded successfully")
except OSError:
    print("⚠️  SpaCy model not found. Install with: python -m spacy download en_core_web_sm")
    nlp = None

for text in sample_posts:
    doc = nlp(text)

    # Named Entity Recognition
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    entity_types = Counter([ent[1] for ent in entities])

    print(f"\n  • Named entities found: {len(entities)}")
    for entity_type, count in entity_types.most_common(5):
        print(f"    - {entity_type}: {count}")

    # Show some examples
    if entities:
        print(f"  • Entity examples: {entities[:3]}")

    # Lemmatization (more accurate than stemming)
    lemmas = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    lemma_freq = Counter(lemmas)
    common_lemmas = lemma_freq.most_common(5)
    print(f"  • Most common lemmas: {[f'{lemma}({count})' for lemma, count in common_lemmas]}")

    # Dependency parsing (show relationships)
    print("  • Sample dependencies:")
    for token in doc[:10]:  # First 10 tokens
        if token.dep_ != 'punct':
            print(f"    - {token.text} --{token.dep_}--> {token.head.text}")