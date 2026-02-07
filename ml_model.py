from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample dataset
commands = [
    "open google", "search youtube", "play music", "what is the time",
    "tell me a joke", "get weather", "open notepad"
]
actions = [
    "open_google", "search_youtube", "play_music", "get_time",
    "tell_joke", "get_weather", "open_notepad"
]

# Train the model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(commands)
model = LogisticRegression()
model.fit(X, actions)

def predict_action(query):
    X_test = vectorizer.transform([query])
    return model.predict(X_test)[0]
