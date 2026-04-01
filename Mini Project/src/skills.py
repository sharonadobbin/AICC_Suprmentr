# This module contains functions to load a list of skills from a file and extract skills from the text of resumes and job descriptions.

def load_skills(file_path):
    with open(file_path, "r") as f:
        return [line.strip().lower() for line in f]


def extract_skills(text, skills_list):
    found = []
    for skill in skills_list:
        if skill in text:
            found.append(skill)
    return list(set(found))