import random
from typing import List, Dict
from src.profile_schema import (
    DOMAINS,
    INDUSTRIES,
    SENIORITY_LEVELS,
    SKILLS_BY_DOMAIN,
    GOALS_BY_DOMAIN,
    MENTORING_TOPICS_BY_DOMAIN,
    FORMATS,
    LANGUAGES,
    MEETING_FREQUENCY
)


def pick_seniority_for_mentor() -> str:
    return random.choices(
        ["senior", "lead", "head"],
        weights=[0.5, 0.35, 0.15],
        k=1
    )[0]


def pick_seniority_for_mentee() -> str:
    return random.choices(
        ["junior", "middle", "senior"],
        weights=[0.45, 0.4, 0.15],
        k=1
    )[0]


def generate_mentor_profile(mentor_id: int) -> Dict:
    domain = random.choice(DOMAINS)
    industry = random.choice(INDUSTRIES)
    seniority = pick_seniority_for_mentor()
    skills = random.sample(SKILLS_BY_DOMAIN[domain], k=random.randint(4, 6))
    topics = random.sample(MENTORING_TOPICS_BY_DOMAIN[domain], k=random.randint(2, 4))
    formats = random.sample(FORMATS, k=random.randint(1, 2))
    language = random.choice(LANGUAGES)
    frequency = random.choice(MEETING_FREQUENCY)
    experience_years = random.randint(5, 15)

    return {
        "id": f"mentor_{mentor_id}",
        "role": "mentor",
        "domain": domain,
        "industry": industry,
        "seniority": seniority,
        "skills": skills,
        "topics": topics,
        "experience_years": experience_years,
        "formats": formats,
        "language": language,
        "meeting_frequency": frequency
    }


def generate_mentee_profile(mentee_id: int) -> Dict:
    target_domain = random.choice(DOMAINS)
    industry_interest = random.choice(INDUSTRIES)
    current_seniority = pick_seniority_for_mentee()
    skills = random.sample(SKILLS_BY_DOMAIN[target_domain], k=random.randint(2, 4))
    goals = random.sample(GOALS_BY_DOMAIN[target_domain], k=random.randint(2, 3))
    formats = random.sample(FORMATS, k=random.randint(1, 2))
    language = random.choice(LANGUAGES)
    frequency = random.choice(MEETING_FREQUENCY)

    return {
        "id": f"mentee_{mentee_id}",
        "role": "mentee",
        "target_domain": target_domain,
        "industry_interest": industry_interest,
        "current_seniority": current_seniority,
        "skills": skills,
        "development_goals": goals,
        "preferred_formats": formats,
        "language": language,
        "meeting_frequency": frequency
    }


def generate_mentors(n: int = 100) -> List[Dict]:
    return [generate_mentor_profile(i + 1) for i in range(n)]


def generate_mentees(n: int = 200) -> List[Dict]:
    return [generate_mentee_profile(i + 1) for i in range(n)]


def mask_profile(profile: Dict, completeness: float = 1.0) -> Dict:
    """
    completeness=1.0 -> профиль полный
    completeness=0.75 -> примерно 75% полей заполнено
    """
    masked = profile.copy()
    protected_fields = {"id", "role"}

    candidate_fields = [k for k in masked.keys() if k not in protected_fields]
    fields_to_keep = max(1, int(len(candidate_fields) * completeness))
    kept = set(random.sample(candidate_fields, fields_to_keep))

    for field in candidate_fields:
        if field not in kept:
            masked[field] = None

    return masked
