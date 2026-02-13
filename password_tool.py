"""
Password Security Tool - INFO 153B/253B Lab 1

Analyze password strength and generate secure passwords.

"""

import string
import random

# Common weak passwords
COMMON_PASSWORDS = [
    "123456", "password", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley"
]


# ============================================
# TODO 1: Password Strength Checker
# ============================================

def check_password_strength(password):
    """
    Analyze password and return strength score.
    
    Scoring:
    - 8+ characters: 20 points
    - 12+ characters: 30 points (instead of 20)
    - Has number: 20 points
    - Has uppercase: 20 points
    - Has lowercase: 20 points
    - Has special char (!@#$%): 20 points
    - Not in common list: 10 points
    
    Returns:
        dict with keys: "password", "score", "strength", "feedback"
        
    Strength levels:
    - 0-39: "Weak"
    - 40-69: "Medium"
    - 70-100: "Strong"
    
    Example:
        >>> result = check_password_strength("Hello123!")
        >>> result["score"]
        90
        >>> result["strength"]
        "Strong"
    
    Hint: Use .isdigit(), .isupper(), .islower() and string.punctuation
    """
    points = 0
    strength = ''
    feedback = []
    feedback.append("Elements Missing: ")
    
    hasNum = False 
    hasCap = False 
    hasLow = False
    hasSpecial = False 

    length = len(password)
    if length >= 8: 
        points+=20
        if length >= 12: 
            points+=10
    else: 
        feedback.append('too few characters')
    i = 0
    while i < length: 
        if not hasNum and password[i].isdigit(): 
            points+=20
            hasNum = True
        if not hasCap and password[i].isupper():
            points+=20
            hasCap = True 
        if not hasLow and password[i].islower():
            points+=20
            hasLow = True
        if not hasSpecial and password[i] in string.punctuation:
            points+=20
            hasSpecial = True
        i+=1
    if password not in COMMON_PASSWORDS:
        points+=10
    if not hasNum: 
        feedback.append('numerical character')
    if not hasCap:
        feedback.append('uppercase letter')
    if not hasLow: 
        feedback.append('lowercase letter')
    if not hasSpecial:
        feedback.append('special character')

    if points <= 39: 
        strength = "Weak"
    elif points >=40 and points <=69:
        strength = "Medium"
    else: 
        strength = "Strong"

    password_return = {
        "password": password, 
        "score": points,
        "strength": strength,
        "feedback": feedback
    }

    return password_return

# ============================================
# TODO 2: Password Generator
# ============================================

def generate_password(length=12, use_special=True):
    """
    Generate a random secure password.
    
    Requirements:
    - Include uppercase, lowercase, and numbers
    - Include special characters if use_special=True
    - Minimum length: 8
    
    Args:
        length: Password length (default 12)
        use_special: Include special characters (default True)
    
    Returns:
        str: Generated password
    
    Example:
        >>> pwd = generate_password(10, True)
        >>> len(pwd)
        10
    
    Hint: Use string.ascii_uppercase, string.ascii_lowercase, 
          string.digits, and random.choice()
    """
    # TODO: Implement this function    
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    num = random.choice(string.digits)
    password = [upper,lower,num]

    all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    if use_special:
        special = random.choice(string.punctuation)
        password.append(special)
        all_chars += string.punctuation
    true_len = max(length, 8)
    for i in range(true_len - len(password)):
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return "".join(password)
    

# ============================================
# Simple Testing
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("PASSWORD SECURITY TOOL - Quick Test")
    print("=" * 60 + "\n")
    
    # Check if functions are implemented
    try:
        # Test TODO 1
        result = check_password_strength("TestPassword123!")
        
        if result is None:
            print("❌ TODO 1 not implemented yet (returned None)")
            print("\nImplement check_password_strength() and try again.\n")
            exit()
        
        if not isinstance(result, dict):
            print("❌ TODO 1 should return a dictionary")
            exit()
        
        required_keys = ["password", "score", "strength", "feedback"]
        missing_keys = [key for key in required_keys if key not in result]
        
        if missing_keys:
            print(f"❌ TODO 1 missing keys in return dict: {missing_keys}")
            exit()
        
        print("✓ TODO 1 implemented - returns correct structure")
        print(f"  Example: '{result['password']}' → {result['strength']} ({result['score']}/100)")
        
        # Test TODO 2
        pwd = generate_password(12, True)
        
        if pwd is None:
            print("\n❌ TODO 2 not implemented yet (returned None)")
            print("\nImplement generate_password() and try again.\n")
            exit()
        
        if not isinstance(pwd, str):
            print("\n❌ TODO 2 should return a string")
            exit()
        
        print(f"\n✓ TODO 2 implemented - generates passwords")
        print(f"  Example: '{pwd}' (length: {len(pwd)})")
        
        # Success!
        print("\n" + "=" * 60)
        print("✅ Both functions implemented!")
        print("=" * 60)
        print("\nRun the full test suite to verify correctness:")
        print("  python test_password_tool.py")
        print()
        
    except AttributeError as e:
        print(f"❌ Error: {e}")
        print("\nMake sure both functions are defined.\n")
    except Exception as e:
        print(f"❌ Error running functions: {e}")
        print("\nCheck your implementation and try again.\n")