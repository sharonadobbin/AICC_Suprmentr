# to match the resume with the job description and calculate the similarity score and missing skills

from pyexpat import model

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(vectors)[0][1]
    return round(score * 100, 2)


def missing_skills(resume_skills, jd_skills):
    return list(set(jd_skills) - set(resume_skills))

def skill_match_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0

    matched = len(set(resume_skills) & set(jd_skills))
    total = len(jd_skills)

    return (matched / total) * 100

def final_score(tfidf_score, skill_score):
    # Weight skills more (important)
    return round((0.4 * tfidf_score) + (0.6 * skill_score), 2)