import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-z0-9.+# ]', ' ', text) 
    words = text.split()

    stop_words = set(stopwords.words("english"))
    words = [w for w in words if w not in stop_words]

    return " ".join(words)
