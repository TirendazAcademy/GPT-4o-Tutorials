from openai import OpenAI
import re
from pathlib import Path
import webbrowser

client = OpenAI()

response = client.responses.create(
    model = "gpt-5-nano",
    input="Make me landing page for a retro-games store. Make it light, more pastel coloured & flowery(think Mario, not cyberpunk)"
)

def extract_html_from_text(text: str):
    """Extract an HTML code block from text; fallback to first code block, else full text."""
    html_block = re.search(r"```html\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
    if html_block:
        result = html_block.group(1)
        return result
    any_block = re.search(r"```\s*(.*?)\s*```", text, re.DOTALL)
    if any_block:
        result = any_block.group(1)
        return result
    return text

response_text = response.output_text 
html_code= extract_html_from_text(response_text)

with open("index_clean_light.html", "w", encoding="utf-8") as f:
    f.write(html_code)

file_path = Path("index_clean_light.html").resolve()

# file:///home/kullanici/proje/index_clean.html

webbrowser.open(file_path.as_uri())

