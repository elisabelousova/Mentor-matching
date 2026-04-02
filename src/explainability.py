from typing import Dict


def explain_match(mentor: Dict, mentee: Dict, components: Dict) -> str:
    reasons = []

    if components["domain"] > 0:
        reasons.append("совпадает профессиональная область")
    if components["skills"] > 0:
        reasons.append("есть пересечение по навыкам")
    if components["goals"] > 0:
        reasons.append("цели менти соответствуют темам менторства")
    if components["seniority"] == 1.0:
        reasons.append("уровень ментора подходит для развития менти")
    if components["format"] > 0:
        reasons.append("совпадает предпочтительный формат взаимодействия")
    if components["language"] > 0:
        reasons.append("совпадает язык общения")
    if components["industry"] > 0:
        reasons.append("совпадает интерес к индустрии")

    if not reasons:
        return "Рекомендация слабая: выраженных совпадений по ключевым признакам не найдено."

    return "Рекомендация выдана, потому что " + ", ".join(reasons) + "."
