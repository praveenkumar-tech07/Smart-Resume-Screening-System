# Smart Resume Screening System

**Smart Resume Screening System** is a Python-based tool that automatically parses, scores, and ranks resumes against a job description using natural language processing (NLP) and similarity models. Recruiters can quickly shortlist candidates based on keyword relevance, skills matching, and semantic similarity.

---

## 📌 Table of Contents

- 🔍 Project Overview  
- 🚀 Features  
- 🧠 How It Works  
- 🛠 Tech Stack  
- 📁 Project Structure  
- ⚙️ Installation & Setup  
- 🧪 Usage  
- 📊 Output & Interpretation  
- 🧩 How It Works Internally  
- 📌 Limitations & Future Work  
- 🙌 Contributing  
- 📝 License

---

## 🔍 Project Overview

The Smart Resume Screening System automates the screening of candidate resumes based on job descriptions. It extracts key information from resumes (skills, education, experience) and calculates similarity scores using text preprocessing and vector similarity techniques. Resumes can be ranked from most relevant to least relevant, saving HR teams significant time and bias in screening.

---

## 🚀 Features

✔️ Resume parsing from text or supported document formats  
✔️ Text preprocessing (tokenization, cleaning, stopword removal)  
✔️ Similarity scoring between resumes and job descriptions  
✔️ Ranking of candidates for job relevance  
✔️ Optional OCR support for scanned resumes  
✔️ Easily extensible with NLP models

---

## 🧠 How It Works

1. **Input**: Upload one or more resumes and a job description.  
2. **Parsing**: Extract raw text from resumes (PDF, DOCX, or scanned).  
3. **Preprocessing**: Clean, tokenize, and vectorize text.  
4. **Similarity Model**: Compute similarity against job description.  
5. **Output**: Ranked list of candidates + relevant scoring metrics.

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| NLP & Text | NLTK / spaCy |
| Similarity Model | TF-IDF / Cosine Similarity / Optional Embeddings |
| Resume Parsing | OCR / Python libraries |
| CLI / UI | Command-line or Flask/Streamlit (if implemented) |

---

## 📁 Project Structure

Smart-Resume-Screening-System/
│
├── main.py # Entry point of the application
├── resume_parser.py # Logic to extract text from resumes
├── text_preprocessing.py # Clean and normalize text
├── similarity_model.py # Similarity scoring functions
├── resume_screening.py # Screening pipeline
├── ocr_resume_extractor.py # Optional OCR module
├── domain_skills.json # Domain skills dataset (sample)
├── job_description.txt # Example job description
├── resumes/ # Sample resumes for testing
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ Installation & Setup

Run the following commands step-by-step in your terminal to set up the project:

```
# 1. Clone the repository
git clone https://github.com/praveenkumar-tech07/Smart-Resume-Screening-System.git
cd Smart-Resume-Screening-System

# 2. Create a virtual environment (optional but recommended)
python -m venv venv

# 3. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install required Python packages
pip install -r requirements.txt

# 5. (Optional) Install Tesseract OCR engine if you plan to use OCR functionality
# - Windows: https://github.com/tesseract-ocr/tesseract/wiki
# - macOS (using Homebrew): brew install tesseract
# - Linux (Debian/Ubuntu): sudo apt-get install tesseract-ocr

# 6. (Optional) Download language data if needed for Tesseract
# Example for English: https://github.com/tesseract-ocr/tessdata
```
## 🧪 Usage

### Run the application
```
python main.py --resumes ./resumes --job job_description.txt
```
### 💡 Replace ./resumes with your own folder of resumes and job_description.txt with the target job description.

## Sample Output
After running, the tool will:

✔ Extract text from all resumes
✔ Compare each resume with the job description
✔ Print a ranked list with similarity scores

Example:
Rank  Resume                     Score
1     John_Doe_Resume.pdf        0.92
2     Jane_Smith_CV.pdf          0.88

##📊 Output & Interpretation
| Score Range | Interpretation  |
| ----------- | --------------- |
| 0.80 – 1.00 | Highly relevant |
| 0.60 – 0.79 | Good match      |
| 0.40 – 0.59 | Partial match   |
| < 0.40      | Low relevance   |
Higher scores indicate better alignment with job requirements based on text analysis.

##🧩 How It Works Internally

Parsing Logic
The system uses text extraction libraries to read content from documents. OCR handles images/scanned files.

Preprocessing

Lowercaser

Tokenizer

Stopword removal

Optional Lemmatization

Similarity Model
The default model is TF-IDF with cosine similarity. You can swap in embedding-based approaches (e.g., Sentence Transformers) for deeper semantic matching.

##📌 Limitations & Future Work

###❗ Current limitations

Does not support all file types

Basic NLP — may misinterpret complex formatting

No GUI (unless added)

###✨ Future upgrades

Streamlit / Web UI

Use of transformer embeddings (BERT, SBERT)

Database integration for bulk resumes

##🙌 Contributing

Contributions are welcome! 🤝

1.Fork the repo

2.Create a branch: git checkout -b feature/my-feature

3.Commit your changes: git commit -m "feat: add something"

4.Push and open a Pull Request

5.Follow code style and include tests
