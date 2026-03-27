# -------------------------------
# ML Idea Generator (Menu Driven)
# -------------------------------

# Data structure
ml_ideas = {
    "College": {
        "1": {
            "type": "Prediction",
            "problem": "Student Performance Prediction",
            "input": "Attendance, assignment scores, exam marks, study hours",
            "output": "Predicted final grade or pass/fail status",
            "process": "Collect student data, preprocess it, train a model, and predict performance."
        },
        "2": {
            "type": "Recommendation",
            "problem": "Course Recommendation System",
            "input": "Student interests, past courses, grades",
            "output": "Recommended courses",
            "process": "Analyze preferences and use recommendation algorithms."
        }
    },

    "Healthcare": {
        "1": {
            "type": "Prediction",
            "problem": "Disease Prediction System",
            "input": "Symptoms, medical history, test results",
            "output": "Predicted disease",
            "process": "Train classification models on medical data."
        },
        "2": {
            "type": "Risk Analysis",
            "problem": "Hospital Readmission Prediction",
            "input": "Patient history, treatment data",
            "output": "Chance of readmission",
            "process": "Analyze past records and build predictive models."
        }
    },

    "Shopping": {
        "1": {
            "type": "Recommendation",
            "problem": "Product Recommendation System",
            "input": "User browsing and purchase history",
            "output": "Suggested products",
            "process": "Use collaborative filtering techniques."
        },
        "2": {
            "type": "Prediction",
            "problem": "Customer Churn Prediction",
            "input": "Customer activity and behavior",
            "output": "Likelihood of leaving",
            "process": "Train classification models to detect churn."
        }
    }
}


# -------------------------------
# Main Program
# -------------------------------
def main():
    print("=== MACHINE LEARNING IDEA GENERATOR ===\n")

    while True:
        # Domain Selection
        print("Select Domain:")
        print("A. College")
        print("B. Healthcare")
        print("C. Shopping")

        domain_choice = input("Enter choice (A/B/C): ").upper()

        if domain_choice == "A":
            domain = "College"
        elif domain_choice == "B":
            domain = "Healthcare"
        elif domain_choice == "C":
            domain = "Shopping"
        else:
            print("Invalid choice. Try again.\n")
            continue

        # Problem Type Selection
        print(f"\nSelected Domain: {domain}")
        print("Select Problem Type:")

        for key, value in ml_ideas[domain].items():
            print(f"{key}. {value['type']}")

        problem_choice = input("Enter choice: ")

        if problem_choice not in ml_ideas[domain]:
            print("Invalid choice. Try again.\n")
            continue

        idea = ml_ideas[domain][problem_choice]

        # Display Idea
        print("\n--- ML IDEA GENERATED ---\n")
        print("Domain:", domain)
        print("Problem:", idea["problem"])
        print("\nInput:", idea["input"])
        print("Output:", idea["output"])
        print("\nProcess:")
        print(idea["process"])

        # Repeat Option
        again = input("\nGenerate another idea? (yes/no): ").lower()
        if again != "yes":
            print("\nExiting Idea Generator.")
            break


# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    main()