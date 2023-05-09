import openai
from src.parse_affirmation import parse_affirmation
from src.unstable import unstable
from src.html import html
message_history = []
def generate_bot_response(input):
    message_history.append({"role": "user", "content": input})

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message_history
    )

    reply_content = completion.choices[0].message.content

    search_words = ["Guide Being", "Title", "Guide", "Text"]

    if any(word in reply_content for word in search_words):
        json_data = parse_affirmation(reply_content)
        affirmation_data = json.loads(json_data)
        title = affirmation_data["Title"].rstrip(",")
        prompt = affirmation_data["Image"]
        guide_being = affirmation_data["Guide Being"].rstrip(",")
        text = affirmation_data["Text"]
        output_dir = f"./out/{title}"
        image_path = f"{output_dir}/image/{guide_being}.jpg"
        os.makedirs(output_dir, exist_ok=True)

        with open(f"{output_dir}/{title}.json", "w") as individual_file:
            individual_file.write(json_data)

        with open("./out/json_master.json", "a") as master_file:
            master_file.write(json_data + "\n")

        print(json_data)
        print(prompt)

        unstable(title, guide_being, prompt)
        html(title, text, image_path)
    message_history.append({"role": "assistant", "content": reply_content})

    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history)-1, 2)]
    return response
