import re

def assess_password_strength(password):
    # Initialize the score
    score = 0
    feedback = []

    # Check length
    length = len(password)
    if length < 8:
        feedback.append("Password is too short. Try to use at least 8 characters.")
    elif length <= 12:
        score += 1
        feedback.append("Password length is reasonable, but longer passwords are more secure.")
    else:
        score += 2
        feedback.append("Good password length.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for digits
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character (e.g., !, @, #, $, etc.).")

    # Determine password strength
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    # Compile feedback
    if strength != "Very Strong":
        feedback.append("Consider making your password stronger by following the suggestions above.")

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }

# Example usage
password = input("Enter a password to assess: ")
result = assess_password_strength(password)
print(f"Password Strength: {result['strength']}")
print("Feedback:")
for comment in result['feedback']:
    print(f"- {comment}")
