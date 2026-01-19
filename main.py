from resume_parser import extract_resume_text
from text_preprocessing import clean_text
from resume_screening import ResumeScreeningSystem
import json


# -----------------------------
# Load Domain Skills
# -----------------------------
with open("domain_skills.json", "r") as f:
    domain_skills = json.load(f)

domains = list(domain_skills.keys())

print("\nAvailable Engineering Domains:")
for i, domain in enumerate(domains, start=1):
    print(f"{i}. {domain}")

# -----------------------------
# User Selects Domain
# -----------------------------
choice = int(input("\nSelect a domain number: "))
selected_domain = domains[choice - 1]

print(f"\nSelected Domain: {selected_domain}")

# -----------------------------
# Load Resume
# -----------------------------
resume_path = "resumes/Resume.pdf"   
resume_text = extract_resume_text(resume_path)
resume_text = clean_text(resume_text)
print("Resume text length:", len(resume_text))
print(resume_text[:300])


# -----------------------------
# Load Job Description
# -----------------------------
with open("job_description.txt", "r") as f:
    job_description = clean_text(f.read())

# -----------------------------
# Resume Screening
# -----------------------------
system = ResumeScreeningSystem()

score = system.screen_resume(
    resume_text=resume_text,
    job_description=job_description,
    domain=selected_domain
)

missing_skills = system.get_skill_gap(resume_text, selected_domain)

# -----------------------------
# Output
# -----------------------------
print("\n===== Resume Screening Result =====")
print(f"Domain           : {selected_domain}")
print(f"Match Score      : {score}%")

if missing_skills:
    print("Missing Skills   :", ", ".join(missing_skills))
else:
    print("Missing Skills   : None (Excellent match!)")

