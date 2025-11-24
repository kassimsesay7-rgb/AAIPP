def calculate_average(scores):
    total = 0
    for s in scores:
        total += s
    return total / len(scores)

def find_highest(scores):
    return max(scores)

def find_lowest(scores):
    return min(scores)

def process_scores(scores):
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)
   #example usage:
if __name__ == "__main__":
    sample_scores = [85, 92, 78, 90, 88, 76, 95, 89]
    print("Sample Scores:", sample_scores)
    avg_score = calculate_average(sample_scores)
    highest_score = find_highest(sample_scores)
    lowest_score = find_lowest(sample_scores)
    print("Average Score:", avg_score)
    print("Highest Score:", highest_score)
    print("Lowest Score:", lowest_score)
    print("\nUsing process_scores function for same scores:")
    process_scores(sample_scores)


