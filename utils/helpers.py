from .validator import (
    validate_marks,
    validate_year,
    validate_phone,
    validate_email,
    validate_roll_no,
    validate_name,
    validate_department,
    validate_section
)

def get_valid_input(prompt, validator, converter):
    while True:
        try:
            raw_val = input(prompt).strip()
            converted_val = converter(raw_val)       
            valid_val = validator(converted_val)        
            return valid_val      
        except ValueError as e:
                print(f"❌ {e}\n")

def get_valid_updt_input(prompt, validator, converter,old_val):
    while True:
        try:
            raw_val = input(prompt).strip()
            if raw_val == "":
                 return old_val
            converted_val = converter(raw_val)       
            valid_val = validator(converted_val)        
            return valid_val      
        except ValueError as e:
                print(f"❌ {e}\n")
   