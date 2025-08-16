# AI Ethics Checker – Interactive Version


**Description:**  
A Python tool to detect potential ethical issues in text using AI. This interactive version allows users to input text directly, receive an ethical report, and save results in CSV and JSON formats.


**Features:**  
- Detects toxic, offensive, or harmful content.  
- Provides clear warnings or confirms if text seems safe.  
- Interactive text input for real-time analysis.  
- Saves results automatically in CSV and JSON files.  
- Easy to extend with other ethical checks or AI models.  


**Installation:**  
Install required packages with pip:
pip install -r requirements.txt


**Requirements:**
Python 3.10+

transformers

torch

pandas

Usage:

Run the notebook or script.

Enter the text you want to analyze.

View the ethical report in the console.

Results are saved automatically in ethics_report.csv and ethics_report.json.


**Example:**
Enter text to analyze for ethical issues: I hate this group of people and want them to disappear.
Ethics Report:
⚠️ TOXIC detected with confidence 0.87
⚠️ INSULT detected with confidence 0.76

✅ Results saved to ethics_report.csv and ethics_report.json


**License:**
MIT License – free to use and modify.


**Author:**
Angelo Sorte – exploring AI ethics with Python.
