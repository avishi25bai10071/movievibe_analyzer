import pandas as pd
import re
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

#To remove unwanted letters and spaces
def preprocess_review(txt):
    txt = txt.lower()
    txt = re.sub(r'<.*?>', '', txt)
    txt = re.sub(r'[^a-z0-9\s.!?]', '', txt)
    txt = re.sub(r'\s+', ' ', txt).strip()
    return txt

#modeltraining
def initialize_ai():
    print("Hi! I'm Your MOvie Vibe Analyzer")
    
    # loading dataset
    try:
        df = pd.read_csv('IMDB Dataset.csv')
        df = df.sample(20000) 
        df['label'] = df['sentiment'].map({'positive': 1, 'negative': 0})
        mode1 = "ADVANCED (Kaggle Dataset)"
        text_col = 'review'
    except FileNotFoundError:
        print("Dataset not found, switching to a small demo dataset...")
        # if no dataset found..
        data = {
            'text': ['love it', 'great', 'amazing', 'bad', 'terrible', 'waste'],
            'label': [1, 1, 1, 0, 0, 0]
        }
        df = pd.DataFrame(data)
        mode1 = "BASIC (Built-in Data)"
        text_col = 'text'

    # Cleaning text before feeding into model
    # otherwise accuracy drops
    df[text_col] = df[text_col].apply(preprocess_review)
    vect = TfidfVectorizer(ngram_range=(1, 2),stop_words='english')
    X = vect.fit_transform(df[text_col])
    
    model1 = LogisticRegression()
    model1.fit(X, df['label'])
    
    return vect, model1, mode1

#THE TERMINAL LOOP
def main():
    vect1, model2, mode2 = initialize_ai()
    
    while True:
        clearscreen()
        print(f"Movie Vibe Checker [Mode: {mode2}]")
        print("Type 'exit' to quit.")
        
        input1 = input("\nEnter a movie review: ").strip()
        
        if input1.lower() == 'exit':
            print("Goodbye!")
            break
        
        if not input1:
            continue

        # Vibe_Prediction
        cleaned_text = preprocess_review(input1)
        vec = vect1.transform([cleaned_text])
        prediction1 = model2.predict(vec)[0]
        prob = model2.predict_proba(vec)[0]

        # Final Prediction with Confidence%
        if prediction1 == 1:
            print(f"Result: Nice! This review sounds Positive")
            print(f"Confidence: {prob[1]:.1%}") 
        else:
            print(f"Result: This review seems Negative")
            print(f"Confidence: {prob[0]:.1%}")
        
        choice = input("\nPress Enter to continue or type 'exit' to quit: ")
        if choice.lower() == 'exit':
            break

if __name__ == "__main__":
    main()