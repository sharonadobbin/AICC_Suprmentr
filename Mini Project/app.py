# Main application file to run the resume and job description matching process. It uses functions from various modules to extract text, preprocess it, extract skills, compute similarity, and identify missing skills.

from src.parser import extract_text_from_pdf, extract_text_from_txt
from src.preprocess import clean_text
from src.skills import load_skills, extract_skills
from src.matcher import compute_similarity, missing_skills, skill_match_score, final_score
from src.utils import get_top_keywords

import config

# File paths
resume_path = config.RESUME_PATH
jd_path = config.JD_PATH
skills_path = config.SKILLS_PATH

# Load files
resume_text = extract_text_from_pdf(resume_path)
jd_text = extract_text_from_txt(jd_path)

# Preprocess
resume_text = clean_text(resume_text)
jd_text = clean_text(jd_text)

# Load skills list
skills_list = load_skills(skills_path)

# Extract skills
resume_skills = extract_skills(resume_text, skills_list)
jd_skills = extract_skills(jd_text, skills_list)

# Similarity score
tfidf_score = compute_similarity(resume_text, jd_text)
skill_score = skill_match_score(resume_skills, jd_skills)

score = final_score(tfidf_score, skill_score)

# Missing skills
missing = missing_skills(resume_skills, jd_skills)

# JD keyword parameter
top_keywords = get_top_keywords(jd_text, top_n=config.TOP_N_KEYWORDS)

# Output
print("\n===== Resume Analysis =====\n")
print(f"Match Score: {score}%\n")

print("Resume Skills:", resume_skills)
print("JD Skills:", jd_skills)

print("\nMissing Skills:", missing)

print("\nTop JD Keywords:", top_keywords)

print(f"TF-IDF Score: {tfidf_score}%")
print(f"Skill Match Score: {skill_score}%")
print(f"\nFinal Match Score: {score}%\n")