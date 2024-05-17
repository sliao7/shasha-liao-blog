import os
import markdown
import re
from textblob import TextBlob
import nltk
nltk.download('punkt')


for (root, dirs, file) in os.walk(os.curdir):
    for f in file:
        if '.md' in f:
            md_file = os.path.join(root, f)
            print(f)


with open(md_file, 'r') as file:
    text = file.read()

text_b = TextBlob(text)

md_file

re.sub(r'http\S+', '', text)

dir(text_b)
text_b.tags()

text_b.words