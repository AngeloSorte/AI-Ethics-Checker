"""
AI Ethics Checker – Interactive Script
Detects potential ethical issues in text and saves results in CSV and JSON.
"""

# Step 1: Import necessary libraries
import pandas as pd
import json

# Step 2: Define ethics check function
def check_ethics(text):
    """
    Simulated ethical check function.
    Returns a list of warnings if text may be harmful.
    """
    report = []
    
    # Simple keyword-based example (expandable)
    keywords = {
        "hate": "TOXIC",
        "kill": "VIOLENCE",
        "stupid": "INSULT"
    }
    
    for word, label in keywords.items():
        if word.lower() in text.lower():
            report.append(f"⚠️ {label} detected for '{word}'")
    
    if not report:
        report.append("✅ No obvious ethical issues detected")
    
    return report

# Step 3: Interactive input and save results
def analyze_and_save():
    """
    Interactively input text, analyze ethics, and save to CSV/JSON.
    """
    text = input("Enter text to analyze for ethical issues: ")
    report = check_ethics(text)
    
    print("\nEthics Report:")
    for line in report:
        print(line)
    
    # Save results to CSV
    df = pd.DataFrame({"text": [text], "report": [", ".join(report)]})
    df.to_csv("ethics_report.csv", index=False)
    
    # Save results to JSON
    with open("ethics_report.json", "w") as f:
        json.dump({"text": text, "report": report}, f, indent=4)
    
    print("\n✅ Results saved to ethics_report.csv and ethics_report.json")

# Step 4: Run script
if __name__ == "__main__":
    analyze_and_save()
