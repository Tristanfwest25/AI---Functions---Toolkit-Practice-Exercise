
# A simple toolkit with functions for calculating averages, finding max and min, counting occurrences, checking palindromes, and creating reports.


def calculate_average(numbers):
    # Takes a list of numbers, returns the average. Returns 0 if the list is empty.
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max_and_min(numbers):
    # Takes a list of numbers, returns a tuple (max_value, min_value). Do NOT use the built-in max() and min()
    if not numbers:
        return None, None
    #loop through numbers to find max and min
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num

def count_occurrences(items, target):
    # Takes a list and a target value, returns how many times the target appears in the list.
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count

def is_palindrome(text):
    #  Takes a string, returns True if it reads the same forward and backward (case-insensitive, ignoring spaces).
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

def create_report(title, scores):
    #  Takes a report title and a list of scores. Uses calculate_average and find_max_and_min internally. Returns a formatted string report with the title, average score, max score, and min score.
    average_score = calculate_average(scores)
    max_score, min_score = find_max_and_min(scores)
    report = f"Report: {title}\n"
    report += f"Average Score: {average_score:.2f}\n"
    report += f"Max Score: {max_score}\n"
    report += f"Min Score: {min_score}\n"
    return report

#test section

if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]
    
    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))
    
    #Edge cases
    
    print("\nEdge case - empty list:")
    empty_list = []
    print(f"\nAverage: {calculate_average(empty_list)}")
    print(f"Max/Min: {find_max_and_min(empty_list)}")
    
    print("\nEdge Case - count occurrences with muliple target appearances:")
    test_items = [1, 2, 3, 2, 4, 2, 5]
    print(f"\nCount of 2: {count_occurrences(test_items, 2)}")
    
    print("\nEdge case - palindrome fuctionality with spaces, single characters and mixed case:")
    print(f"\n'A man a plan a canal Panama' palindrome: {is_palindrome('A man a plan a canal Panama')}")
    print(f"' ' palindrome: {is_palindrome(' ')}")
    print(f"'a' palindrome: {is_palindrome('a')}")
    print(f"'No lemon, no melon' palindrome: {is_palindrome('No lemon, no melon')}")
    