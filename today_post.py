
import os
import json
import random
import base64
from datetime import date
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
IMAGE_SIZE = "1024x1024"

client = OpenAI(api_key=OPENAI_API_KEY)


QUOTES = [
    {
        "style": "discipline",
        "lines": [
            "“One day” isn’t a plan.",
            "“Today” is."
        ],
        "caption": "Everyone wants progress. Few want today."
    },
    {
        "style": "consistency",
        "lines": [
            "Consistency isn’t loud.",
            "It’s boring.",
            "That’s why it works."
        ],
        "caption": "Silent effort compounds."
    },
    {
        "style": "mindset",
        "lines": [
            "You don’t need motivation.",
            "You need direction."
        ],
        "caption": "Clarity beats hype."
    },
    {
        "style": "late_night",
        "lines": [
            "Nobody sees this part.",
            "That’s why it matters."
        ],
        "caption": "Quiet progress hits different."
    },
    {
        "style": "focus",
        "lines": [
            "Do less.",
            "But do it daily."
        ],
        "caption": "Consistency > intensity."
    }
]


def get_todays_post():
    return random.choice(QUOTES)


def build_image_prompt(lines, style):
    base_prompt = """
    cinematic photography, vertical instagram format,
    soft grain, shallow depth of field,
    minimal aesthetic, moody lighting,
    clean serif typography, high contrast text,
    no watermark
    """

    style_scenes = {
        "discipline": "man walking alone in city at night, hoodie, blurred street lights",
        "consistency": "gym mirror selfie, focused expression, muted colors",
        "late_night": "empty road at sunset, calm cinematic sky",
        "mindset": "desk setup, laptop glow, dark room, late night work",
        "focus": "minimal desk, notebook, coffee, soft shadows"
    }

    text_overlay = " ".join(lines)

    return f"""
    {base_prompt},
    scene: {style_scenes.get(style, 'cinematic minimal scene')},
    text overlay: '{text_overlay}'
    """

def generate_image(prompt, save_path):
    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size=IMAGE_SIZE
    )

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    with open(save_path, "wb") as f:
        f.write(image_bytes)


def create_today_folder():
    today = str(date.today())
    path = f"output/{today}"
    os.makedirs(path, exist_ok=True)
    return path

def save_text(folder, filename, content):
    with open(os.path.join(folder, filename), "w", encoding="utf-8") as f:
        f.write(content)


def main():
    print("💬 Say something...")
    user_input = input("You: ").lower()

    if "today" not in user_input:
        print("❌ Try saying: today's post")
        return

    post = get_todays_post()

    image_prompt = build_image_prompt(
        post["lines"],
        post["style"]
    )

    folder = create_today_folder()

    save_text(folder, "post.txt", "\n".join(post["lines"]))
    save_text(folder, "caption.txt", post["caption"])
    save_text(folder, "prompt.txt", image_prompt)

    generate_image(image_prompt, f"{folder}/image.png")

    print("\n📌 TODAY'S POST\n")
    print("\n".join(post["lines"]))
    print("\nCaption:")
    print(post["caption"])
    print(f"\n📁 Saved in: {folder}")


if __name__ == "__main__":
    main()
