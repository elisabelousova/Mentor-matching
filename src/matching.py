from typing import Dict, List, Tuple


SENIORITY_SCORE = {
    "junior": 1,
    "middle": 2,
    "senior": 3,
    "lead": 4,
    "head": 5
}


DEFAULT_WEIGHTS = {
    "domain": 0.25,
    "skills": 0.20,
    "goals": 0.20,
    "seniority": 0.10,
    "format": 0.10,
    "language": 0.05,
    "industry": 0.10
}


def safe_list(value):
    return value if isinstance(value, list) else []


def jaccard_similarity(list_a: List[str], list_b: List[str]) -> float:
    set_a = set(list_a)
    set_b = set(list_b)
    if not set_a or not set_b:
        return 0.0
    return len(set_a & set_b) / len(set_a | set_b)


def domain_match(mentor: Dict, mentee: Dict) -> float:
    if mentor.get("domain") is None or mentee.get("target_domain") is None:
        return 0.0
    return 1.0 if mentor["domain"] == mentee["target_domain"] else 0.0


def industry_match(mentor: Dict, mentee: Dict) -> float:
    if mentor.get("industry") is None or mentee.get("industry_interest") is None:
        return 0.0
    return 1.0 if mentor["industry"] == mentee["industry_interest"] else 0.0


def skills_overlap(mentor: Dict, mentee: Dict) -> float:
    return jaccard_similarity(
        safe_list(mentor.get("skills")),
        safe_list(mentee.get("skills"))
    )


def goal_match(mentor: Dict, mentee: Dict) -> float:
    return jaccard_similarity(
        safe_list(mentor.get("topics")),
        safe_list(mentee.get("development_goals"))
    )


def seniority_fit(mentor: Dict, mentee: Dict) -> float:
    mentor_s = mentor.get("seniority")
    mentee_s = mentee.get("current_seniority")

    if mentor_s is None or mentee_s is None:
        return 0.0

    mentor_score = SENIORITY_SCORE[mentor_s]
    mentee_score = SENIORITY_SCORE[mentee_s]

    if mentor_score > mentee_score:
        return 1.0
    if mentor_score == mentee_score:
        return 0.5
    return 0.0


def format_fit(mentor: Dict, mentee: Dict) -> float:
    mentor_formats = set(safe_list(mentor.get("formats")))
    mentee_formats = set(safe_list(mentee.get("preferred_formats")))
    if not mentor_formats or not mentee_formats:
        return 0.0
    return 1.0 if len(mentor_formats & mentee_formats) > 0 else 0.0


def language_fit(mentor: Dict, mentee: Dict) -> float:
    if mentor.get("language") is None or mentee.get("language") is None:
        return 0.0
    return 1.0 if mentor["language"] == mentee["language"] else 0.0


def compute_match_score(mentor: Dict, mentee: Dict, weights: Dict = None) -> Tuple[float, Dict]:
    weights = weights or DEFAULT_WEIGHTS

    components = {
        "domain": domain_match(mentor, mentee),
        "skills": skills_overlap(mentor, mentee),
        "goals": goal_match(mentor, mentee),
        "seniority": seniority_fit(mentor, mentee),
        "format": format_fit(mentor, mentee),
        "language": language_fit(mentor, mentee),
        "industry": industry_match(mentor, mentee)
    }

    total_score = sum(components[key] * weights[key] for key in components)
    return total_score, components


def rank_mentors_for_mentee(mentee: Dict, mentors: List[Dict], top_k: int = 3, weights: Dict = None):
    scored = []

    for mentor in mentors:
        score, components = compute_match_score(mentor, mentee, weights=weights)
        scored.append({
            "mentee_id": mentee["id"],
            "mentor_id": mentor["id"],
            "score": round(score, 4),
            "components": components
        })

    scored = sorted(scored, key=lambda x: x["score"], reverse=True)
    return scored[:top_k]
