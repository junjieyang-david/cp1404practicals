"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
LOWEST_SCORES = 0
HIGHEST_SCORES = 100
EXCELLENT_SCORES = 90
PASS_SCORES = 50
score = float(input("Enter score:"))
if LOWEST_SCORES <= score <= HIGHEST_SCORES:
    if score >= EXCELLENT_SCORES:
        message = "excellent"
    elif score >= PASS_SCORES:
        message = "pass"
    else:
        message = "bad"
else:
    message = "invalid value"
print(message)
