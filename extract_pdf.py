import urllib.request
import json
import os
import urllib.parse
import sys

# Attempting to install pypdf if not present
try:
    import pypdf
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
    import pypdf

reader = pypdf.PdfReader("ADVANCE-TRACK.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Text extracted successfully.")
