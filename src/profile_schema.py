DOMAINS = [
    "product management",
    "analytics",
    "data science",
    "ux research",
    "ux/ui design",
    "software engineering",
    "marketing",
    "project management"
]

INDUSTRIES = [
    "edtech",
    "fintech",
    "e-commerce",
    "healthtech",
    "b2b saas",
    "marketplaces",
    "media",
    "enterprise software"
]

SENIORITY_LEVELS = [
    "junior",
    "middle",
    "senior",
    "lead",
    "head"
]

SKILLS_BY_DOMAIN = {
    "product management": [
        "jtbd", "roadmapping", "prioritization", "ab testing",
        "retention", "unit economics", "sql", "analytics"
    ],
    "analytics": [
        "sql", "python", "dashboards", "statistics",
        "ab testing", "data visualization", "excel", "power bi"
    ],
    "data science": [
        "python", "machine learning", "feature engineering", "statistics",
        "nlp", "recommendation systems", "model evaluation", "pandas"
    ],
    "ux research": [
        "interviews", "usability testing", "survey design", "jtbd",
        "research synthesis", "personas", "cjm", "insight generation"
    ],
    "ux/ui design": [
        "figma", "wireframing", "prototyping", "design systems",
        "user flows", "heuristic evaluation", "accessibility", "ui patterns"
    ],
    "software engineering": [
        "python", "javascript", "api", "databases",
        "system design", "testing", "git", "backend"
    ],
    "marketing": [
        "performance marketing", "content strategy", "crm",
        "segmentation", "email marketing", "positioning", "analytics", "copywriting"
    ],
    "project management": [
        "stakeholder management", "agile", "scrum", "roadmapping",
        "risk management", "planning", "communication", "delivery"
    ]
}

GOALS_BY_DOMAIN = {
    "product management": [
        "switch to product", "improve product thinking", "learn experimentation",
        "understand metrics", "grow to senior product role"
    ],
    "analytics": [
        "improve sql", "learn product analytics", "understand dashboards",
        "improve statistics", "learn ab testing"
    ],
    "data science": [
        "learn machine learning", "understand recommendation systems",
        "improve python", "build ml portfolio", "learn model evaluation"
    ],
    "ux research": [
        "learn research methods", "improve usability testing",
        "conduct better interviews", "switch to ux research", "improve synthesis"
    ],
    "ux/ui design": [
        "improve figma", "build portfolio", "learn user flows",
        "switch to design", "improve prototyping"
    ],
    "software engineering": [
        "improve backend skills", "learn system design",
        "switch to engineering", "improve coding", "learn api development"
    ],
    "marketing": [
        "learn performance marketing", "improve crm skills",
        "understand attribution", "switch to marketing", "improve positioning"
    ],
    "project management": [
        "improve planning", "learn stakeholder management",
        "grow to pm role", "improve delivery management", "switch to project management"
    ]
}

MENTORING_TOPICS_BY_DOMAIN = {
    domain: goals[:] for domain, goals in GOALS_BY_DOMAIN.items()
}

FORMATS = ["online", "offline", "hybrid"]
LANGUAGES = ["ru", "en"]
MEETING_FREQUENCY = ["weekly", "biweekly", "monthly"]
