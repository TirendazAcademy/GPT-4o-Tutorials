from openai import OpenAI
import re
from pathlib import Path
import webbrowser

client = OpenAI()

response = client.responses.create(
    model = "gpt-5",
    input="Make me a snake game. It should be futuristic, neon, cyberpunk style. Make sure the typography is suitably cool."
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

with open("snake_game_gpt_5.html", "w", encoding="utf-8") as f:
    f.write(html_code)

file_path = Path("snake_game_gpt_5.html").resolve()

# file:///home/kullanici/proje/index_clean.html

webbrowser.open(file_path.as_uri())

