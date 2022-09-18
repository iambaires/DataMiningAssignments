# -------------------------------------------------------------------------
# AUTHOR: William A Baires
# FILENAME: HW1
# SPECIFICATION: Submission for Assignment #1
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: ~3 hours
# -----------------------------------------------------------*/
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from IPython.display import display
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Defining the documents
doc1 = "Soccer is my favorite sport"
doc2 = "I like sports and my favorite one is soccer"
doc3 = "I support soccer at the olympic games"
doc4 = "I do like soccer, my favorite sport in the olympic games"

# Use the following words as terms to create your document matrix
# [soccer, my, favorite, sport, I, like, one, support, olympic, game]
terms = ['soccer', 'my', 'favorite', 'sport', 'I', 'like', 'one', 'support', 'olympic', 'games']
frequencyList = []
docs = [doc1, doc2, doc3, doc4]
vec = CountVectorizer(vocabulary=terms,
                      lowercase=False,
                      analyzer="word", tokenizer=None,
                      preprocessor=None,
                      stop_words=None,
                      token_pattern=r"(?u)\b\w+\b")
X = vec.fit_transform(docs)
df = pd.DataFrame(X.toarray(), columns=vec.get_feature_names_out())
display(df)



# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors only
# Use cosine_similarity([X, Y, Z]) to calculate the pairwise similarities between multiple vectors
cdf = cosine_similarity(df)
print()
display(cdf)
print()


# Print the highest cosine similarity following the template below
# The most similar documents are: doc1 and doc2 with cosine similarity = x
# --> Add your Python code here
mask = np.ones(cdf.shape, dtype=bool)
np.fill_diagonal(mask, 0)
max_similarity = cdf[mask].max()

break_loop = False
for i in range(len(cdf)):
    for j in range(len(cdf[i])):
        if round(cdf[i][j], 3) == round(max_similarity, 3):
            print("The most similar documents are doc" + str(i) + " and doc" + str(j)
                  + " with cosine similarity = " + str(round(max_similarity, 3)))
            break_loop = True
            break
    if break_loop:
        break



