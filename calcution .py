# Define formative and summative assignments with their respective scores and weights
formative_assignments = [
    {"name": "Assignment 1", "score": 85, "weight": 20},  # example weights
    {"name": "Formative 2", "score": 90, "weight": 30},
    {"name": "Formative 3", "score": 88, "weight": 10}
]

summative_assignments = [
    {"name": "Summative 1", "score": 92, "weight": 25},
    {"name": "Summative 2", "score": 80, "weight": 15}
]

# Function to calculate weighted score for a group of assignments
def calculate_weighted_score(assignments, max_weight):
    total_weight = sum(assignment["weight"] for assignment in assignments)
    if total_weight > max_weight:
        raise ValueError(f"The cumulative weight of assignments exceeds {max_weight}%.")

    weighted_score = sum((assignment["score"] * assignment["weight"] / max_weight) for assignment in assignments)
    return weighted_score

# Calculate and validate formative and summative scores
try:
    formative_score = calculate_weighted_score(formative_assignments, max_weight=60)
    summative_score = calculate_weighted_score(summative_assignments, max_weight=40)
    
    # Total overall score
    overall_score = formative_score + summative_score
    
    print(f"Formative Score (weighted): {formative_score:.2f}")
    print(f"Summative Score (weighted): {summative_score:.2f}")
    print(f"Overall Score: {overall_score:.2f}")

except ValueError as e:
    print(e)
