# Student FAQ Chatbot

## Overview

This project is a simple AI-based chatbot that helps students find answers from their lecture notes quickly. Instead of reading the entire PDF, a user can ask a question and the system will return the most relevant text from the document.

The goal of this project is to demonstrate how semantic search can be used to improve information retrieval in an academic setting.

---

## Features

* Accepts questions in natural language
* Searches lecture notes intelligently
* Returns the most relevant answer
* Fast and efficient document search
* Works without any paid APIs

---

## How It Works

The system follows a structured process:

1. **Load the Document**
   The AI notes PDF is loaded into the program.

2. **Split the Text**
   The document is divided into smaller parts so that searching becomes more accurate.

3. **Convert Text into Vectors**
   Each chunk of text is transformed into numerical representations using an embedding model.

4. **Store in a Vector Database**
   These vectors are stored in FAISS, which allows very fast similarity searching.

5. **Search and Retrieve**
   When a question is asked, the system compares it with stored vectors and returns the closest matching answer.

---

## Technologies Used

* Python
* LangChain
* FAISS
* Sentence Transformers

---

## Project Structure

```
AI_notes.pdf        -> Source document  
app.py              -> Implementation  
README.md           -> Documentation  
```

---

## Setup Instructions

### Install Dependencies

```python
pip install langchain langchain-community sentence-transformers faiss-cpu pypdf
```

### Add the PDF

Place the lecture notes in the project folder and rename it to:

```
AI_notes.pdf
```

### Run the Project

Execute the notebook cells in order.
After running, type a question such as:

```
What is Artificial Intelligence?
```

The system will display the most relevant answer from the notes.

---

## What I Learned

* Basics of semantic search
* How vector databases work
* Document-based chatbot design
* Practical use of NLP concepts

---

## Future Scope

* Add a simple web interface
* Allow multiple documents
* Improve answer accuracy
* Deploy as a web app

---

## Author

Name:   Priyanshu Mangla
Course: B.Tech CSE 6P 
