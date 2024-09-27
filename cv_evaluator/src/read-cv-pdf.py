import urllib.request
from io import BytesIO

import nltk
import PyPDF2
import textract
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("stopwords")

print("Downloading CV...")
