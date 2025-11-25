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

```
Home Page
![Home](images/App.png)
![Home](images/App_1.png)

Summary Output
![Summary](images/Output_1.png)
![Summary](images/Output_2.png)
![Summary](images/Output_3.png)

```


Just create an images/ folder in your repo and place the screenshots there.

# 🚀 How It Works (In Simple Words)

* You enter or upload your text.

* The app breaks the text into sentences.

* It finds which words appear most frequently (after removing stopwords & punctuation).

* It scores each sentence based on those important words.

* It picks the top sentences and generates a short summary — without changing the original meaning.

This method is called extractive summarization, meaning it only selects important sentences instead of generating new ones.

# 💻 How to Run the Project
* 1️⃣ Install Dependencies
pip install streamlit spacy pdfplumber python-docx
python -m spacy download en_core_web_sm


Or install using requirements.txt:

streamlit
spacy
pdfplumber
python-docx

* 2️⃣ Run the App
streamlit run SpaCy_app.py


This will open the app in your browser (usually at http://localhost:8501
).

# 📂 Project Structure

This is the complete structure of the Text Summarizer (spaCy + Streamlit) project:

Text-Summarizer/
│
├── README.md                         # Project documentation
├── requirements.txt                  # Required Python packages
├── SpaCy_app.py                      # Main Streamlit application
├── Day69_SpaCy_Text_Summarization_Project.ipynb    # Notebook for experiments
│
├── images/                           # Screenshots used in the README
│     ├── App.png
│     ├── App_1.png
│     ├── Output_1.png
│     ├── Output_2.png
│     ├── Output_3.png



# 🧩 Features You Can Add (Future Enhancements)

* Abstractive summarization using models like BART or T5

* Dark mode in UI

* SBERT/TextRank-based summarization

* Options like keyword extraction, readability score, etc.

# 🙋‍♀️ Why I Built This

I created this project as part of my learning journey in NLP and Data Science.
It helped me understand:

* Text preprocessing

* Sentence scoring

* Lemmatization

* Building small web apps using Streamlit

If you’re also learning NLP, this project is a great starting point.

# 📬 Contact

Kummara Lahari
📧 lahari11kummara@gmail.com