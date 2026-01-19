import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_domain_skills():
    with open("domain_skills.json", "r") as f:
        return json.load(f)

def calculate_score(resume_text, job_desc, domain):
    domain_skills = load_domain_skills()
    skills_text = " ".join(domain_skills[domain])

    documents = [
        resume_text,
        job_desc,
        skills_text
    ]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    resume_vec = tfidf_matrix[0]
    jd_vec = tfidf_matrix[1]
    skills_vec = tfidf_matrix[2]

    jd_similarity = cosine_similarity(resume_vec, jd_vec)[0][0]
    skill_similarity = cosine_similarity(resume_vec, skills_vec)[0][0]

    final_score = (0.6 * jd_similarity) + (0.4 * skill_similarity)

    return round(final_score * 100, 2)
