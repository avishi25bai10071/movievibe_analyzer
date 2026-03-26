# movievibe_analyzer
A CLI-based sentiment analysis tool that classifies movie reviews as positive or negative using TF-IDF and Logistic Regression.
## Overview
The project addresses the challenge of manually analyzing the vast volume of online movie reviews. By automating this process, the system provides accurate sentiment classification, reducing manual effort and helping to understand audience opinions more effectively.
## Objective
The primary goals for developing the MovieVibe Analyzer include:
- Build a sentiment analysis model: Create a functional machine learning model capable of interpreting text data.  
- Automated Classification: Develop a system that can quickly and accurately classify reviews as either positive or negative using AI and NLP.  
- Process and Clean Data: Implement a preprocessing pipeline to clean raw text data for better model performance.  
- Provide Real-time Results: Ensure the system offers quick and accurate predictions for the user in a live environment.  
- Reduce Manual Effort: Address the difficulty of manually analyzing large volumes of online movie reviews by automating the process.
## Features
- Automated Classification: Quickly identifies reviews as either Positive or Negative.
- Confidence Scoring: Provides a percentage-based confidence score for every prediction.
- Real-time CLI: Features a continuous loop in the terminal for testing multiple reviews instantly.  
- Robust Preprocessing: Includes a custom cleaning pipeline to handle HTML tags, punctuation, and case normalization.  
- Context Awareness: Uses TF-IDF with bigrams (two-word combinations) to better understand phrases like "not bad".
## Methodology & Tech Stack
The project is built using a modern Python data science stack:  
- Language: Python  
- Data Handling: Pandas (used for managing the IMDB 50K dataset)  
- Text Processing: Regex (re library) for cleaning raw text  
- Vectorization: TF-IDF (Term Frequency-Inverse Document Frequency) to convert text into numerical format  
- Machine Learning: Logistic Regression via Scikit-learn for effective binary classification 
## How It Works
1. User enters a movie review
2. Text is cleaned (lowercase, remove unwanted characters)
3. Cleaned text is converted into numerical form using TF-IDF
4. Logistic Regression model predicts sentiment
5. Result is shown as Positive or Negative with confidence score
6. Program continues until user exits
## Installation & Setup
1. Requires Python and basic libraries
2. Open project in a code editor
3. Install required packages
4. Run the program from terminal
5. Uses IMDB dataset if available, otherwise demo data
## Implementation Details
- Data Preparation: The model is trained on a subset of 10,000 to 20,000 random reviews from the IMDB 50K dataset to balance training speed and accuracy.  
- Classification Logic: The system processes the text and predicts sentiment; if the probability score is above 0.5, it is classified as POSITIVE.  
- Model Accuracy: The use of Logistic Regression provides a simple yet effective solution for binary classification tasks.
## Results
The model successfully classifies movie reviews as positive or negative with an approximate accuracy of 85–90% on the IMDB dataset. It provides real-time predictions through a simple CLI interface along with a confidence score, making the results easy to understand. Overall, the system effectively reduces the effort required to manually analyze large numbers of reviews.

<img width="1192" height="355" alt="Screenshot 2026-03-26 135654" src="https://github.com/user-attachments/assets/d7090957-09c8-4916-a382-806d909b435b" />
<img width="1205" height="355" alt="Screenshot 2026-03-26 135743" src="https://github.com/user-attachments/assets/683f05e6-d8b7-448a-9121-fd20ef920d0f" />

## Future Scope
- Advanced Models: Implementing Deep Learning architectures like LSTM or BERT to detect complex sentiments such as sarcasm or neutrality.  
- Web Interface: Transitioning from a CLI to a web-based application using Streamlit for an enhanced user experience.  
- Expanded Sentiments: Moving beyond binary classification to include a "Neutral" category.
## Limitations
- Only classifies reviews as positive or negative
- Cannot detect sarcasm or complex emotions
- Accuracy depends on training data
- Limited understanding due to TF-IDF
- CLI-based (no graphical interface)
## Conclusion
MovieVibe Analyzer shows how Artificial Intelligence and NLP can be used to easily analyze movie reviews. It gives quick and accurate results, reducing the need for manual work and helping to understand audience opinions better. Overall, this project demonstrates how machine learning can be applied in real-life situations and can be further improved to build more advanced sentiment analysis systems in the future.
## Author
NAME - AVISHI PATIDAR <BR>
REGISTRATION NO. - 25BAI10071
