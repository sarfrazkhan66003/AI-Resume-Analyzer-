# AI Resume Analyzer 🚀

- An AI-powered Resume Analysis System built using Streamlit and Natural Language Processing (NLP) that automatically extracts key information from resumes, evaluates profile strength, predicts job roles, and provides intelligent skill & career recommendations.
- This project simulates a real-world HR Tech product, designed for students, job seekers, and recruiters to analyze resumes efficiently and improve employability.

# 📌 Why This Project Matters (Importance)

- In today’s competitive job market:
  - Recruiters spend only 6–8 seconds scanning a resume.
  - Many candidates are rejected due to missing keywords, skills gaps, or poor structure.
  - Manual resume screening is time-consuming and biased.

- 🎯 AI Resume Analyzer solves this problem by:
  - Automating resume parsing using NLP
  - Providing objective resume scoring
  - Suggesting missing skills aligned with industry standards
  - Helping candidates become ATS-friendly

# 🌟 Key Features

### 🧠 Intelligent Resume Parsing
  - Extracts Name, Email, Phone Number, Education, Skills, Degree & Resume Length
  - Uses spaCy NLP pipelines & PyResparser
  - Supports PDF resumes
 
### 📊 Resume Scoring System
- Calculates a Resume Score based on:
  - Completeness of sections
  - Skill presence
  - Content relevance
- Helps users understand resume strength instantly

### 🎯 Job Role Prediction
- Predicts suitable job profiles such as:
  - Data Scientist
  - Web Developer
  - Android / iOS Developer
  - UI/UX & more
- Based on extracted skills and resume content

### 📈 Skill Gap & Match Analysis
  - Compares user skills with industry-required skills
  - Displays Match Percentage
  - Recommends missing skills for improvement

### 🎓 Course & Learning Recommendations
  - Curated YouTube courses & learning resources
  - Personalized based on predicted job role
  - Helps users upskill efficiently

# 🛠️ Tech Stack

  | Layer         | Technology               |
  | ------------- | ------------------------ |
  | Frontend      | Streamlit                |
  | Backend       | Python                   |
  | NLP           | spaCy, PyResparser, NLTK |
  | Database      | MySQL                    |
  | Visualization | Matplotlib, Plotly       |
  | PDF Parsing   | PDFMiner                 |

# ⚙️ System Architecture & Algorithm

### 🔁 Resume Processing Flow
1. Resume Upload
2. Text Extraction
  - PDFMiner extracts raw text from PDF
3. NLP Processing
  - Tokenization
  - Named Entity Recognition (NER)
  - Skill extraction using keyword matching + noun chunks
4. Scoring Algorithm
- Score assigned based on:
  - Sections found
  - Skill count
  - Resume length
5. Job Role Prediction
  - Mapping extracted skills to predefined role clusters
6. Recommendations Engine
  - Missing skills
  - Courses & learning resources
7. Data Storage
  - User details saved in MySQL
8. Visualization (Admin Panel)

# 🗄️ Database Design & Storage

### 📁 Tables Used
1. user_data
- Stores:
  - Name
  - Email
  - Phone
  - Resume Score
  - Predicted Job Role
  - Skills
  - Timestamp
  - 
2. user_feedback
- Stores:
  - User Name
  - Email
  - Feedback Text
  - Rating
  - Timestamp
- ✔️ Enables analytics & performance tracking
- ✔️ Helps improve system quality over time

# 🧑‍💼 Admin Dashboard (Analytics Panel)

### 🔐 Admin Capabilities
  - View total users & resumes analyzed
  - Analyze resume score distribution using Pie Charts
  - Track most common job roles
  - Download user data as CSV
  - Review user feedback

### 📊 Helps admins understand:
  - User engagement
  - Skill trends
  - System effectiveness

# 💬 Feedback Processing System

1. User submits feedback via UI
2. Feedback is validated & stored in MySQL
3. Admin can review feedback from dashboard
4. Insights used to:
  - Improve recommendations
  - Enhance scoring logic
  - Upgrade user experience

# 📋 Prerequisites

- Python 3.8 – 3.10
- MySQL Server
- pip / virtualenv

# 📁 Project Structure

    AI-Resume-Analyzer/
    │
    ├── App.py                  # Main Streamlit application
    ├── resume_parser.py        # Resume parsing & NLP logic
    ├── courses.py              # Course & video recommendations
    ├── Stored_files/           # Uploaded resumes
    ├── requirements.txt
    └── README.md

# 🚀 Future Enhancements

- ATS keyword optimization
- Deep Learning–based resume scoring
- Job description matching
- Multi-language resume support
- Cloud deployment (AWS / Azure)
- Authentication & role-based access
  
# 🤝 Contributing

- Contributions are welcome!
- Feel free to open issues, submit pull requests, or suggest improvements.

# 👨‍💻 Author

## Mohammad Sarfraz Khan
## 📌 Data Science
