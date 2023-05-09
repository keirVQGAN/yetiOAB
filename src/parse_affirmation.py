import re

def parse_affirmation(text):
    guide_creature_match = re.search(r"Guide Being:\s+(.*?)\s+Title:", text, re.MULTILINE | re.DOTALL)
    title_match = re.search(r"Title:\s+(.*?)\s+Text:", text, re.MULTILINE | re.DOTALL)
    affirmation_text_match = re.search(r"Text:\s+(.*?)\s+Image:", text, re.MULTILINE | re.DOTALL)
    image_match = re.search(r"Image:\s+(.*)", text, re.MULTILINE | re.DOTALL)

    if guide_creature_match and title_match and affirmation_text_match and image_match:
        affirmation_data = {
            "Guide Being": guide_creature_match.group(1).strip(),
            "Title": title_match.group(1).strip(),
            "Text": affirmation_text_match.group(1).strip(),
            "Image": image_match.group(1).strip()
        }

        return json.dumps(affirmation_data, indent=4)
    else:
        print("Failed to parse text")
        return None