import random
import sys

# --- Project 1: Simple Input & Conditional Logic (Guessing Game) ---

def run_guessing_game():
    """
    Demonstrates taking simple string/integer input and using conditional logic.
    """
    print("\n" + "="*50)
    print("Project 1: Number Guessing Game")
    print("="*50)
    
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # Loop to allow multiple guesses
    while True:
        try:
            # 1. Take input from the user. input() returns a string.
            guess_str = input("Guess the secret number (1-10) or type 'exit': ").strip().lower()
            
            # Check for the exit command
            if guess_str == 'exit':
                print(f"Game ended. The secret number was {secret_number}.")
                return
            
            # 2. Convert the input string to an integer
            guess = int(guess_str)
            
            # 3. Validate the input range
            if not 1 <= guess <= 10:
                print("🚨 Invalid input. Please guess a number between 1 and 10.")
                continue

            # 4. Use conditional logic (if/elif/else) to check the result
            if guess == secret_number:
                print(f"🎉 Correct! You guessed {secret_number}!")
                break
            elif guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
                
        # 5. Error Handling: Catch exceptions if the input cannot be converted to an integer
        except ValueError:
            print("❌ That wasn't a valid number. Please enter a whole number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

# --- Project 2: Validated Numeric Input (BMI Calculator) ---

def get_validated_float_input(prompt):
    """
    Helper function to continuously prompt the user until a valid positive float is entered.
    This demonstrates the power of a loop combined with error handling (try/except).
    """
    while True:
        try:
            # Take input and immediately strip whitespace
            value_str = input(prompt).strip()
            value = float(value_str)
            
            # Check if the value is positive
            if value <= 0:
                print("⚠️ Value must be a positive number.")
                continue
            return value
        except ValueError:
            # This handles cases where input() cannot be converted to a float
            print("❌ Invalid input. Please enter a numeric value (e.g., 75.5 or 1.75).")

def calculate_bmi():
    """
    Calculates Body Mass Index (BMI) using two validated inputs.
    BMI = weight (kg) / height^2 (m^2)
    """
    print("\n" + "="*50)
    print("Project 2: Body Mass Index (BMI) Calculator")
    print("="*50)
    
    # Get validated input for weight
    weight_kg = get_validated_float_input("Enter your weight in kilograms (kg): ")
    
    # Get validated input for height
    height_m = get_validated_float_input("Enter your height in meters (m): ")
    
    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    
    # Output the result
    print(f"\n✅ Input successful.")
    print(f"Weight: {weight_kg:.1f} kg, Height: {height_m:.2f} m")
    print(f"Your calculated BMI is: {bmi:.2f}")

# --- Project 3: Handling Multiple Inputs (List/Array Data) ---

def analyze_scores():
    """
    Demonstrates taking a string of space-separated values and converting it into a list of numbers.
    """
    print("\n" + "="*50)
    print("Project 3: Data Analysis of Scores")
    print("="*50)

    try:
        # 1. Take a single line of input containing multiple scores
        scores_input = input("Enter a list of scores separated by spaces (e.g., 85 92 78 100): ").strip()
        
        # Check for empty input
        if not scores_input:
            print("No scores entered. Exiting analysis.")
            return

        # 2. Split the input string into a list of strings
        score_strings = scores_input.split()
        
        # 3. Convert all elements in the list from string to integer using map()
        # The int() function is applied to every item in the score_strings list.
        scores = list(map(int, score_strings))
        
        # 4. Perform basic statistical analysis on the resulting list
        
        # Sort the scores for finding median
        scores.sort() 
        
        mean_score = sum(scores) / len(scores)
        min_score = min(scores)
        max_score = max(scores)
        
        # Calculate the median
        n = len(scores)
        if n % 2 == 1:
            median_score = scores[n // 2] # Odd number of elements
        else:
            mid1 = scores[n // 2 - 1]
            mid2 = scores[n // 2]
            median_score = (mid1 + mid2) / 2 # Even number of elements
        
        # 5. Display the results
        print("\n--- Analysis Report ---")
        print(f"Raw Scores: {scores}")
        print(f"Total Count: {n}")
        print(f"Average (Mean) Score: {mean_score:.2f}")
        print(f"Median Score: {median_score:.2f}")
        print(f"Highest Score: {max_score}")
        print(f"Lowest Score: {min_score}")

    except ValueError:
        print("❌ Error: One or more of the entered scores was not a valid whole number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Main Execution Block ---

if __name__ == "__main__":
    # Run all three projects sequentially for practice
    print("--- Starting Input Practice Projects ---")
    run_guessing_game()
    calculate_bmi()
    analyze_scores()
    print("\n--- All Input Projects Complete ---")
