import os
import json
import pandas as pd
import matplotlib.pyplot as plt

from src.data_generation import generate_mentors, generate_mentees
from src.matching import rank_mentors_for_mentee
from src.explainability import explain_match
from src.evaluation import run_fullness_experiment


def ensure_dirs():
    os.makedirs("data/generated", exist_ok=True)
    os.makedirs("data/experiments", exist_ok=True)


def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    ensure_dirs()

    mentors = generate_mentors(120)
    mentees = generate_mentees(80)

    save_json(mentors, "data/generated/mentors.json")
    save_json(mentees, "data/generated/mentees.json")

    example_mentee = mentees[0]
    top_matches = rank_mentors_for_mentee(example_mentee, mentors, top_k=3)

    explanations = []
    for match in top_matches:
        mentor = next(m for m in mentors if m["id"] == match["mentor_id"])
        explanation = explain_match(mentor, example_mentee, match["components"])
        explanations.append({
            "mentee_id": example_mentee["id"],
            "mentor_id": mentor["id"],
            "score": match["score"],
            "explanation": explanation
        })

    explanations_df = pd.DataFrame(explanations)
    explanations_df.to_csv("data/experiments/example_recommendations.csv", index=False)

    results_df = run_fullness_experiment(mentees, mentors)
    results_df.to_csv("data/experiments/fullness_experiment.csv", index=False)

    plt.figure(figsize=(8, 5))
    plt.plot(results_df["completeness"], results_df["avg_precision_at_3"], marker="o")
    plt.xlabel("Profile completeness")
    plt.ylabel("Average Precision@3")
    plt.title("Impact of profile completeness on recommendation quality")
    plt.grid(True)
    plt.savefig("data/experiments/fullness_experiment.png", bbox_inches="tight")
    plt.close()

    print("Project run completed successfully.")
    print("Generated files:")
    print("- data/generated/mentors.json")
    print("- data/generated/mentees.json")
    print("- data/experiments/example_recommendations.csv")
    print("- data/experiments/fullness_experiment.csv")
    print("- data/experiments/fullness_experiment.png")


if __name__ == "__main__":
    main()
