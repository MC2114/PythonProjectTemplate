# Import librries

from pathlib import Path
import matplotlib.pyplot as plt
from wordcloud import WordCloud # To generate word cloud image

def generate_wordcloud(document_dir): 
    # Aggregating texts
    text= ""
    for txt_file in Path(document_dir).glob("*.txt"):
        print("Getting words from file:", txt_file)
        txt_contents = txt_file.read_text()
        text += " " + txt_contents

    # Generating word cloud
    wordcloud = WordCloud(width=800, height=400, max_words=20, colormap="Dark2").generate(text=text)
    return wordcloud


