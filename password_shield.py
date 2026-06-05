import random
import string

def check_password_strength(password):
    """
    Function to evaluate the strength of a given password based on 
    length and character diversity (uppercase, lowercase, digits, special characters).
    """
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    # Calculate the diversity score (max score is 4)
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    # Determine the strength level
    if length >= 12 and score == 4:
        return "🔥 Very Strong"
    elif length >= 8 and score >= 3:
        return "🟢 Strong"
    elif length >= 6 and score >= 2:
        return "🟡 Medium"
    else:
        return "🔴 Weak - Try adding more character types and length!"

def generate_secure_password(length=14):
    """
    Function to generate a highly secure, random password.
    Ensures at least one uppercase, one lowercase, one digit, and one special character.
    """
    if length < 4:
        return "Password length must be at least 4 characters!"
        
    # Combine all available characters
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Guarantee the inclusion of at least one character from each mandatory group
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the remaining length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the list to randomize the position of the mandatory characters
    random.shuffle(password)
    
    # Join the list into a single string and return
    return "".join(password)

# --- Main Program Execution ---
print("=== Advanced Password Generator & Strength Checker ===")

# 1. Generate a complex password automatically
generated_pass = generate_secure_password(16)  # Generates a 16-character password
print(f"\nGenerated Secure Password: {generated_pass}")

# 2. Check the strength of the generated password
strength = check_password_strength(generated_pass)
print(f"Password Security Level: {strength}")

print("\n-----------------------------------------------------")

# 3. Allow the user to test their own password
user_pass = input("Now, enter a password to test its strength: ")
print(f"Your Password Security Level: {check_password_strength(user_pass)}")
