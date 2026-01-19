import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ResumeScreeningSystem:
    def __init__(self, domain_skill_path="domain_skills.json"):
        with open(domain_skill_path, "r") as f:
            self.domain_skills = json.load(f)

        self.vectorizer = TfidfVectorizer(stop_words="english")

    def screen_resume(self, resume_text, job_description, domain):
        if domain not in self.domain_skills:
            raise ValueError("Selected domain not found")

        domain_skill_text = " ".join(self.domain_skills[domain])

        documents = [
            resume_text,
            job_description,
            domain_skill_text
        ]

        tfidf_matrix = self.vectorizer.fit_transform(documents)

        resume_vec = tfidf_matrix[0]
        jd_vec = tfidf_matrix[1]
        skill_vec = tfidf_matrix[2]

        jd_similarity = cosine_similarity(resume_vec, jd_vec)[0][0]
        skill_similarity = cosine_similarity(resume_vec, skill_vec)[0][0]

        final_score = (0.2 * jd_similarity) + (0.8 * skill_similarity)


        return round(final_score * 100, 2)

    def get_skill_gap(self, resume_text, domain):
        resume_words = set(resume_text.lower().split())
        required_skills = set(skill.lower() for skill in self.domain_skills[domain])

        return list(required_skills - resume_words)
