import spacy
from pyresparser import ResumeParser

resume_path = r"C:\Users\DELL\OneDrive\Desktop\Sarfraz\PW Data Science\Project\AI-Resume-Analyzer-main\Uploaded_Resumes\MOHAMMAD SARFRAZ KHAN ATS Resume.pdf"

# Load the official English model
nlp = spacy.load("en_core_web_sm")

# Use pyresparser without passing spacy_model (if your pyresparser version doesn't support it)
resume_data = ResumeParser(resume_path).get_extracted_data()

print(resume_data)
