import os
import sys
from pyresparser import ResumeParser
import pymysql

print("--- Testing Database ---")
try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Sarfraz@0786',
        db='cv',
        port=3306
    )
    print("MySQL Connection: SUCCESS")
    connection.close()
except Exception as e:
    print(f"MySQL Connection: FAILED ({e})")

print("\n--- Testing ResumeParser Class ---\n")
resume_path = r"c:\Users\DELL\OneDrive\Desktop\Sarfraz\PW Data Science\Project\AI-Resume-Analyzer-main\Uploaded_Resumes\Analyzer Test Resume .pdf"
if not os.path.exists(resume_path):
    print(f"Resume file not found: {resume_path}")
else:
    try:
        print("Instantiating ResumeParser...")
        parser = ResumeParser(resume_path)
        print("ResumeParser instantiated SUCCESS.")
        # If we get here, init passed (which loads models)
    except Exception as e:
        print(f"ResumeParser instantiation FAILED: {e}")
        import traceback
        traceback.print_exc()
