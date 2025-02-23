import streamlit as st
import spacy
from textblob import TextBlob
import random

# Load spaCy model for NLP
nlp = spacy.load("en_core_web_sm")

# Predefined interview questions
interview_questions = [
    "Tell me about yourself.",
    "What is your greatest strength?",
    "What is your greatest weakness?",
    "Why do you want to work here?",
    "Where do you see yourself in 5 years?",
    "How do you handle stress and pressure?",
    "Tell me about a time you overcame a challenge.",
    "Why should we hire you?"
]

# Function to evaluate response using NLP and TextBlob
def evaluate_response(response):
    # NLP analysis with spaCy
    doc = nlp(response)
    # Sentiment analysis using TextBlob
    blob = TextBlob(response)
    sentiment = blob.sentiment.polarity

    # Analyze sentence structure (spaCy)
    num_tokens = len(doc)
    num_sentences = len(list(doc.sents))

    # Give feedback based on response length and sentiment
    if num_tokens < 10:
        feedback = "Your response is too short. Try elaborating more."
    elif num_tokens > 40:
        feedback = "Your response is a bit too long. Keep it concise and to the point."
    else:
        feedback = "Your response is well-balanced."

    # Sentiment feedback
    if sentiment > 0.2:
        feedback += " Your answer is positive and confident!"
    elif sentiment < -0.2:
        feedback += " Your answer is a bit negative. Try to keep a positive tone."
    else:
        feedback += " Your answer seems neutral. Try to sound more confident."

    return feedback

# Streamlit UI for the interview simulation
def interview_simulation():
    st.title("Job Interview Simulation created by Shan-e-Ali")
    st.write("Welcome to the Job Interview Simulation. Prepare for common interview questions and get feedback!")

    # Select a random interview question
    question = random.choice(interview_questions)
    st.write(f"**Question**: {question}")

    # User's response (Text input)
    response = st.text_area("Your response:", "", height=200)

    if st.button("Submit Answer (Text)"):
        if response:
            feedback = evaluate_response(response)
            st.write(f"**Feedback**: {feedback}")
        else:
            st.write("Please provide an answer.")

    st.write("Try again to get feedback on your next answer!")

# Run the Streamlit app
if __name__ == "__main__":
    interview_simulation()
