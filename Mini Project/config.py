# Configuration file for the resume and job description matching project. This file contains constants and parameters that can be easily modified to adjust the behavior of the application without changing the core code.

# File paths
RESUME_PATH = "files/resume.pdf"
JD_PATH = "files/jd.txt"
SKILLS_PATH = "data/skills.txt"

# NLP parameters
TOP_N_KEYWORDS = 15          # how many keywords to extract from JD
SIMILARITY_THRESHOLD = 50    # optional: minimum match score

# Skill matching
USE_PARTIAL_MATCH = True     # future enhancement