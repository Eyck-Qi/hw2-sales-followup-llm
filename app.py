import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a professional sales assistant.
Write a concise and professional follow-up email after a client meeting.
Do NOT invent facts.
If the input is unclear, stay neutral and polite.
"""

def generate_email(notes):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": notes}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"""
[API failed: {e}]

Demo output:

Subject: Follow-Up After Our Meeting

Dear Sarah,

Thank you for taking the time to meet with me. I appreciate the opportunity to discuss your interest in our AI dashboard product.

Based on our conversation, I understand that you would like more information about pricing, onboarding, and Shopify integration. As a next step, I will send the pricing details and coordinate a demo for next week.

Please let me know if there is anything else you would like me to include.

Best regards,
Sales Representative
"""


def main():
    print("=== Sales Email Generator ===")
    notes = input("Enter meeting notes:\n")

    email = generate_email(notes)

    print("\n=== Generated Email ===\n")
    print(email)

    with open("output.txt", "w") as f:
        f.write(email)


if __name__ == "__main__":
    main()