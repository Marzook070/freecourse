import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def search(query, num_results):
    # Extract the titles from the JSON data
    texts = [item['Title'] for item in data]

    # Create the vectorizer and transform the titles into a feature matrix
    vectorizer = CountVectorizer()
    features = vectorizer.fit_transform(texts)

    # Transform the query into a feature vector
    query_vector = vectorizer.transform([query])

    # Calculate the cosine similarity between the query vector and the feature matrix
    similarities = cosine_similarity(query_vector, features)

    # Get the indices of the top matching items
    top_indices = similarities.argsort()[0][-num_results:][::-1]

    # Retrieve the top matching items
    top_matches = [data[idx] for idx in top_indices]

    return top_matches
# Load JSON file into the data variable
try:
    with open("freecourse/static/searcher/unique_data.json") as f:
        data = json.load(f)
except:
    with open("/home/freecourse/freecourse/freecourse/static/searcher/unique_data.json") as f:
        data = json.load(f)

# Example usage
def give(query):
    r = []
    l= []
    num_results = 5
    results = search(query, num_results)

    for i in results:
        l.append(i['Title'])

        l.append(i['Link'])

        r.append([l[0],l[1]])

        l.clear()

    final = r
    return final
