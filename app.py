
from flask import Flask, request, render_template
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
import pickle
import nltk
import re


nltk.download('stopwords')
nltk.download('wordnet')


# Remove "\", special symbols, and extra whitespaces

def cleantext(text):

    # removing the "\"
    text = re.sub("'\'", "", text)
    # removing special symbols
    text = re.sub("[^a-zA-Z]", " ", text)
    # removing the whitespaces
    text = ' '.join(text.split())
    # convert text to lowercase
    text = text.lower()

    return text


# Remove the stopwords

def removestopwords(text):
    stop_words = set(stopwords.words('english'))
    removed_stopword = [word for word in text.split() if word not in stop_words]
    return ' '.join(removed_stopword)


# lemmatizing the text

def lemmatizing(text):
    lemma = WordNetLemmatizer()
    lemmatized_sentence = ' '.join(lemma.lemmatize(word) for word in text.split())
    return lemmatized_sentence


# stemming the text,i.e reducing the word size

def stemming(text):
    stemmer = PorterStemmer()
    stemmed_sentence = ' '.join(stemmer.stem(word) for word in text.split())
    return stemmed_sentence


# testing the model

def test(text, model, tfidf_vectorizer):

    text = cleantext(text)
    text = removestopwords(text)
    text = lemmatizing(text)
    text = stemming(text)
    text_vector = tfidf_vectorizer.transform([text])
    predicted = model.predict(text_vector)

    newmapper = {0: 'Fantasy', 1: 'Science Fiction', 2: 'Crime Fiction',
                 3: 'Historical novel', 4: 'Horror', 5: 'Thriller'}


    return newmapper[predicted[0]]


# Loading the model
def load_model():
    try:
        with open('bookgenremodel.pkl', 'rb') as file:
            model = pickle.load(file)

        with open('tfdifvector.pkl', 'rb') as file1:
            tfidf_vectorizer = pickle.load(file1)

        return model, tfidf_vectorizer

    except FileNotFoundError:
        print("Error: Model files not found.")
        return None, None
    except Exception as e:
        print(f"Error loading models: {e}")
        return None, None


app = Flask(__name__)

# Load the model and vectorizer
model, tfidf_vectorizer = load_model()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        mydict = request.form
        text = mydict.get("summary", "")
        if text:
            prediction = test(text, model, tfidf_vectorizer)
        return render_template('index.html', genre=prediction, text=str(text)[:100], showresult=True)
    
    return render_template('index.html')


if __name__ == '__main__':
    if model and tfidf_vectorizer:
        app.run()
    else:
        print("App cannot start without the required models.")
