"""
Email Validator using State Machine Implementation

This module implements an email address validator using a finite state machine (FSM) approach.
The FSM transitions through different states as it processes each character of the email address,
ensuring it follows standard email format: localpart@domain.tld

State Machine Design:
- INIT (0): Initial state, expects start of local part
- LOCAL (1): Processing local part before @ symbol
- AT (2): Found @ symbol, transition to domain
- DOMAIN (3): Processing domain name
- DOT (4): Found dot in domain
- TLD (5): Processing top level domain
- VALID (6): Email successfully validated
- ERROR (-1): Invalid email format detected

Valid transitions:
INIT -> LOCAL -> AT -> DOMAIN -> DOT -> TLD -> VALID
Any invalid character or sequence leads to ERROR state

Author: [Your name]
"""

def validate_email(email):
    # Define states for the finite state machine
    INIT = 0          # Initial state waiting for local part
    LOCAL = 1         # Processing characters in local part
    AT = 2           # Found @ symbol
    DOMAIN = 3       # Processing domain name
    DOT = 4          # Processing dot in domain
    TLD = 5          # Processing top level domain
    VALID = 6        # Email is valid
    ERROR = -1       # Invalid email format
    current_state = INIT
    
    # Define valid character sets for different parts of email
    local_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    domain_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    # Process each character through the state machine
    for char in email:
        if current_state == INIT:
            # Initial state: must start with valid local part character
            if char in local_chars:
                current_state = LOCAL
            else:
                current_state = ERROR
                break
                
        elif current_state == LOCAL:
            # Local part: continue until @ symbol
            if char == '@':
                current_state = AT
            elif char not in local_chars:
                current_state = ERROR
                break
                
        elif current_state == AT:
            # After @ symbol: must have valid domain character
            if char in domain_chars:
                current_state = DOMAIN
            else:
                current_state = ERROR
                break
                
        elif current_state == DOMAIN:
            # Domain: continue until dot
            if char == '.':
                current_state = DOT
            elif char not in domain_chars:
                current_state = ERROR
                break
                
        elif current_state == DOT:
            # After dot: must have valid TLD character
            if char in domain_chars:
                current_state = TLD
            else:
                current_state = ERROR
                break
                
        elif current_state == TLD:
            # TLD: can have another dot (for co.uk style domains) or continue TLD
            if char == '.':
                current_state = DOT
            elif char not in domain_chars:
                current_state = ERROR
                break

    # Final state check: must end in TLD state to be valid
    if current_state == TLD:
        current_state = VALID
        
    return current_state == VALID

def test_email_validator():
    """
    Test suite for email validator
    Tests various email formats including valid and invalid cases
    Returns list of test results
    """
    test_cases = [
        "user@domain.com",           # Valid email
        "test.email@company.co.uk",  # Valid email with multiple dots
        "invalid@domain",            # Invalid - missing TLD
        "@nodomain.com",            # Invalid - missing local part
        "no.at.symbol"              # Invalid - missing @ symbol
    ]
    
    results = []
    for email in test_cases:
        is_valid = validate_email(email)
        results.append(f"Email: {email} -> {'Valid' if is_valid else 'Invalid'}")
    
    return results

# Main execution block
if __name__ == "__main__":
    test_results = test_email_validator()
    for result in test_results:
        print(result)
