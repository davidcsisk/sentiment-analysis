import urllib.request
import sys
from inscriptis import get_text
from textblob import TextBlob  # https://textblob.readthedocs.io/en/dev/quickstart.html

# TexBlob notes: 
# The polarity score is a float within the range [-1.0, 1.0]. 
# The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.

# If no URL argument was passed in, then display a help message and exit
if len(sys.argv) == 1:
   print(f"   Usage: {sys.argv[0]} valid_url")
   print(f"     Example: {sys.argv[0]} https://www.marketwatch.com/latest-news")
   quit()

# Get the argument containing the URL, pull the contents of the URL, and strip the HTML out to leave just text
url = sys.argv[1]
html = urllib.request.urlopen(url).read().decode('utf-8')
text = get_text(html)

# Create a TextBlob object from the text, and display the URL, sentiment polarity, and sentiment subjectivity
tb_text = TextBlob(text)
print(f"URL: {url}...Polarity[-1 to 1]: {tb_text.sentiment.polarity}...Subjectivity[0 to 1]: {tb_text.sentiment.subjectivity}")

