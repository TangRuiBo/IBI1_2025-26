# pseudocode
# 1. Prompt user to input four core parameters: age, weight, gender, creatinine concentration (Cr)
# 2. Input validation logic (if invalid, prompt corrections instead of calculating results):
#    - Age: must be an integer and < 100 years old
#    - Weight: must be a number (int/float) and in the range 20-80 kg
#    - Creatinine concentration (Cr): must be a number (int/float) and in the range 0-100 µmol/l
#    - Gender: only accepts "male" or "female" (case-sensitive, exact match)
# 3. If all inputs are valid, calculate using the Cockcroft-Gault formula:
#    - Male: CrCl = ((140 - age) × weight × 1.23) / creatinine concentration
#    - Female: CrCl = ((140 - age) × weight × 1.23) / creatinine concentration × 0.85
# 4. Print the final Creatine Clearance (CrCl) result; if inputs are invalid, print the problematic variables

def calculate_creatine_clearance():
    # Initialize list to collect error messages for invalid inputs
    error_messages = []
    
   
    try:
        # Age validation (integer, < 100)
        age = int(input("Please enter your age (years): "))
        if age >= 100:
            error_messages.append("Age must be less than 100 years old")
    except ValueError:
        error_messages.append("Age must be an integer (e.g., 25, 40)")
    
    try:
        # Weight validation (number, 20-80 kg)
        weight = float(input("Please enter your weight (kg): "))
        if not (20 <= weight <= 80):
            error_messages.append("Weight must be between 20 and 80 kg")
    except ValueError:
        error_messages.append("Weight must be a number (e.g., 55, 68.5)")
    
    try:
        # Creatinine concentration validation (number, 0-100 µmol/l)
        cr = float(input("Please enter your creatinine concentration (µmol/l): "))
        if not (0 <= cr <= 100):
            error_messages.append("Creatinine concentration must be between 0 and 100 µmol/l")
    except ValueError:
        error_messages.append("Creatinine concentration must be a number (e.g., 80, 95.2)")
    
    # Gender validation (only "male" or "female")
    gender = input("Please enter your gender (male/female): ").strip()
    if gender not in ["male", "female"]:
        error_messages.append("Gender must be either 'male' or 'female' (exact match)")
    
    
    if error_messages:
        # Print error messages if there are invalid inputs
        print("\n❌ Invalid inputs detected. Please correct the following issues:")
        for error in error_messages:
            print(f" - {error}")
    else:
        # Calculate Creatine Clearance using Cockcroft-Gault formula
        # Base calculation (male)
        crcl_base = ((140 - age) * weight * 1.23) / cr
        # Adjust for female (multiply by 0.85)
        if gender == "female":
            crcl = crcl_base * 0.85
        else:
            crcl = crcl_base
        
        # Print result with 2 decimal places for readability
        print(f"\n✅ Your Creatine Clearance (CrCl) is: {crcl:.2f} ml/min")

# Execute the calculator function when the script is run directly
if __name__ == "__main__":
    calculate_creatine_clearance()