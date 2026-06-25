from tkinter import *
from tkinter import scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import nltk

# Download stopwords (first run only)
nltk.download('stopwords')

# -----------------------------
# FAQ QUESTIONS
# -----------------------------
faq_questions = [
    "What is AI",
    "What is Machine Learning",
    "What is Deep Learning",
    "What is Python",
    "What is NLP",
    "What is Data Science",
    "What is ChatGPT",
    "What is a chatbot",
    "What is cloud computing",
    "What is cybersecurity",
    "What is supervised learning",
    "What is unsupervised learning",
    "What is reinforcement learning",
    "What is a neural network",
    "What is TensorFlow",
    "What is Pandas",
    "What is NumPy",
    "What is computer vision",
    "What is face recognition",
    "What is data preprocessing",
    "What is overfitting",
    "What is underfitting",
    "What is a dataset",
    "What is feature engineering",
    "What is classification",
    "What is regression",
    "What is a decision tree",
    "What is random forest",
    "What is KNN",
    "What is logistic regression",
    "What is OpenAI",
    "What is Generative AI",
    "What is prompt engineering",
    "What is automation",
    "What is Internet of Things",
    "What is SQL",
    "What is database",
    "What is API",
    "What is Git",
    "What is GitHub"
]

# -----------------------------
# FAQ ANSWERS
# -----------------------------
faq_answers = [
    "Artificial Intelligence is the simulation of human intelligence in machines.",
    "Machine Learning is a subset of AI that enables systems to learn from data without explicit programming.",
    "Deep Learning is a branch of Machine Learning that uses neural networks with multiple layers.",
    "Python is a high-level programming language widely used for AI, data science, and web development.",
    "NLP stands for Natural Language Processing, which helps computers understand and process human language.",
    "Data Science is the field of extracting meaningful insights from structured and unstructured data.",
    "ChatGPT is an AI language model developed by OpenAI.",
    "A chatbot is a software application that interacts with users through text or voice conversations.",
    "Cloud computing provides computing services such as storage and processing over the internet.",
    "Cybersecurity protects computer systems, networks, and data from cyber threats and attacks.",
    "Supervised learning is a machine learning technique that uses labeled training data.",
    "Unsupervised learning finds hidden patterns in data without using labeled outputs.",
    "Reinforcement learning trains an agent by rewarding desired actions and penalizing undesired actions.",
    "A neural network is a computational model inspired by the structure of the human brain.",
    "TensorFlow is an open-source machine learning framework developed by Google.",
    "Pandas is a Python library used for data manipulation and analysis.",
    "NumPy is a Python library used for numerical computations and array operations.",
    "Computer Vision enables computers to understand and interpret images and videos.",
    "Face recognition identifies or verifies a person using facial features from an image or video.",
    "Data preprocessing involves cleaning, transforming, and preparing data before analysis or model training.",
    "Overfitting occurs when a model learns the training data too well and performs poorly on new data.",
    "Underfitting occurs when a model is too simple to capture patterns in the data.",
    "A dataset is a collection of related data used for analysis or machine learning.",
    "Feature engineering is the process of selecting and transforming variables to improve model performance.",
    "Classification is a machine learning task that predicts categories or class labels.",
    "Regression is a machine learning task that predicts continuous numerical values.",
    "A decision tree is a machine learning algorithm that makes decisions based on a tree-like structure.",
    "Random Forest is an ensemble learning method that combines multiple decision trees.",
    "KNN stands for K-Nearest Neighbors, a simple machine learning algorithm used for classification and regression.",
    "Logistic Regression is a classification algorithm used to predict categorical outcomes.",
    "OpenAI is an artificial intelligence research company that develops advanced AI technologies.",
    "Generative AI creates new content such as text, images, audio, and code.",
    "Prompt engineering is the practice of designing effective prompts to improve AI-generated outputs.",
    "Automation is the use of technology to perform tasks with minimal human intervention.",
    "The Internet of Things connects physical devices to the internet for communication and data exchange.",
    "SQL stands for Structured Query Language and is used to manage relational databases.",
    "A database is an organized collection of data that can be accessed and managed efficiently.",
    "An API allows different software applications to communicate with each other.",
    "Git is a version control system used to track changes in source code.",
    "GitHub is a platform that hosts Git repositories and enables collaboration among developers."
]

# -----------------------------
# NLP PREPROCESSING
# -----------------------------
stop_words = set(stopwords.words('english'))

def preprocess(text):
    words = text.lower().split()

    filtered_words = [
        word for word in words
        if word not in stop_words
    ]

    return " ".join(filtered_words)

processed_questions = [preprocess(q) for q in faq_questions]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)

# -----------------------------
# CHATBOT RESPONSE FUNCTION
# -----------------------------
def get_response():

    user_input = entry_box.get()

    if not user_input.strip():
        return

    chat_area.insert(END, f"You: {user_input}\n")

    processed_input = preprocess(user_input)

    user_vector = vectorizer.transform([processed_input])

    similarity = cosine_similarity(
        user_vector,
        faq_vectors
    )

    best_match_index = similarity.argmax()

    confidence = similarity[0][best_match_index]

    if confidence < 0.3:
        response = "Sorry, I don't understand that question."
    else:
        response = faq_answers[best_match_index]

    chat_area.insert(END, f"Bot: {response}\n\n")

    entry_box.delete(0, END)

    chat_area.see(END)

# -----------------------------
# GUI WINDOW
# -----------------------------
root = Tk()
root.title("FAQ Chatbot")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

# Heading
title_label = Label(
    root,
    text="🤖 FAQ Chatbot",
    font=("Arial", 20, "bold"),
    bg="#f0f0f0"
)
title_label.pack(pady=10)

# Chat Area
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=WORD,
    width=80,
    height=25,
    font=("Arial", 11)
)
chat_area.pack(padx=10, pady=10)

# Welcome Message
chat_area.insert(
    END,
    "Bot: Hello! I am your FAQ Chatbot.\n"
    "Ask me questions about AI, Python, Machine Learning, Data Science, GitHub, etc.\n\n"
)

# Bottom Frame
bottom_frame = Frame(root, bg="#f0f0f0")
bottom_frame.pack(pady=10)

# Input Box
entry_box = Entry(
    bottom_frame,
    width=60,
    font=("Arial", 12)
)
entry_box.grid(row=0, column=0, padx=5)

# Send Button
send_button = Button(
    bottom_frame,
    text="Send",
    command=get_response,
    width=12,
    font=("Arial", 10)
)
send_button.grid(row=0, column=1, padx=5)

# Press Enter to Send
entry_box.bind(
    "<Return>",
    lambda event: get_response()
)

root.mainloop()