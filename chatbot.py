import json
import re
from pathlib import Path

class CustomerSupportBot:
    def __init__(self):
        data_path = Path(__file__).parent / "data" / "faqs.json"
        with open(data_path, "r", encoding="utf-8") as file:
            self.faqs = json.load(file)

    def clean_text(self, text):
        text = text.lower().strip()
        text = re.sub(r"[^a-z0-9\s]", "", text)
        return text

    def get_response(self, message):
        text = self.clean_text(message)

        if any(word in text.split() for word in ["hello", "hi", "hey"]):
            return "Hello! 😊 I'm happy to help. You can ask me about orders, delivery, returns, refunds, payments, or account issues."

        if "thank" in text:
            return "You're very welcome! 😊 If you need anything else, I'm here to help."

        if any(word in text for word in ["bye", "goodbye"]):
            return "Goodbye! 👋 Thank you for contacting customer support."

        best_question = None
        best_score = 0

        for item in self.faqs:
            score = 0
            for keyword in item["keywords"]:
                if keyword in text:
                    score += 1
            if score > best_score:
                best_score = score
                best_question = item

        if best_question and best_score > 0:
            return best_question["answer"]

        return (
            "I'm sorry, I couldn't fully understand your question. 😕 "
            "Please try asking about your order, delivery, return, refund, payment, "
            "or contact our support team for further help."
        )
