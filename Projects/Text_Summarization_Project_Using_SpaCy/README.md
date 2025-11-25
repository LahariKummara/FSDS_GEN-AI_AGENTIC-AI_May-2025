# 📝 Text Summarizer (spaCy + Streamlit)

This project is a simple and clean text summarization app built using spaCy and Streamlit.
You can paste text or upload a file, choose how short you want the summary to be, and the app will instantly generate a clear extractive summary for you.

It’s lightweight, fast, and perfect for learning NLP basics.

# ⭐ What This App Does

* Summarizes text by selecting the most important sentences

* Works with .txt, .pdf, and .docx files

* Lets you choose the summary length

* Uses spaCy for tokenization, lemmatization, and sentence scoring

* Simple, user-friendly Streamlit interface

# 🖼️ Screenshots

You can add your app screenshots here after running the project.
Use this format in your README once you upload images to GitHub:

![App Screenshot](images/App.png)
![App Screenshot](images/App_1.png)
![Summary Output](images/Output_1.png)
![Summary Output](images/Output_2.png)
![Summary Output](images/Output_3.png)


Or if you prefer a caption style:

### Home Page
![Home](images/home_page.png)

### Summary Output
![Summary](images/summary_output.png)


Just create an images/ folder in your repo and place the screenshots there.

# 🚀 How It Works (In Simple Words)

* You enter or upload your text.

* The app breaks the text into sentences.

* It finds which words appear most frequently (after removing stopwords & punctuation).

* It scores each sentence based on those important words.

* It picks the top sentences and generates a short summary — without changing the original meaning.

This method is called extractive summarization, meaning it only selects important sentences instead of generating new ones.

# 💻 How to Run the Project
## 1️⃣ Install Dependencies
pip install streamlit spacy pdfplumber python-docx
python -m spacy download en_core_web_sm


Or install using requirements.txt:

streamlit
spacy
pdfplumber
python-docx

## 2️⃣ Run the App
streamlit run SpaCy_app.py


This will open the app in your browser (usually at localhost:8501).

# 📁 Files in This Project

* SpaCy_app.py – The main Streamlit app

* Day69_SpaCy_Text_Summarization_Project.ipynb – Notebook used for understanding and experimenting with the summarization logic

# 🧩 Features You Can Add (Future Enhancements)

If you want to improve this project further:

* Add abstractive summarization using models like BART or T5

* Add dark mode in UI

* Add SBERT/TextRank-based summarization

* Add options like keyword extraction, readability score, etc.

# 🙋‍♀️ Why I Built This

I created this project as part of my learning journey in NLP and Data Science.
It helped me understand:

* Text preprocessing

* Sentence scoring

* Lemmatization

* Building small web apps using Streamlit

If you’re also learning NLP, this project is a great starting point.

# 📬 Contact/Author

Kummara Lahari
📧 lahari11kummara@gmail.com