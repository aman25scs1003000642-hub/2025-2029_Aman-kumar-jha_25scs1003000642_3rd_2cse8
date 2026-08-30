# Project Explanation – Simple Hinglish

## 1. Project kya hai?

Ye ek Customer Support Chatbot Agent hai. Customer apni problem normal language me type karta hai aur chatbot automatically answer deta hai.

## 2. Python ka use kyu kiya?

Python easy hai aur chatbot, AI, data processing aur web applications ke liye bahut useful hai.

## 3. Streamlit kya karta hai?

Streamlit Python code ko ek simple web application me convert karta hai. Isliye hume HTML/CSS/JavaScript separately nahi likhna pada.

## 4. chatbot.py ka kaam

`CustomerSupportBot` class customer ka message leti hai, usko clean karti hai, FAQ keywords se compare karti hai aur suitable answer return karti hai.

## 5. faqs.json ka kaam

Is file me customer ke common questions aur answers stored hain. Isse hum future me naye questions easily add kar sakte hain.

## 6. app.py ka kaam

Ye main application hai. Ye chatbot ka user interface banata hai aur customer ke messages screen par show karta hai.

## 7. Interview me kya bolna hai?

"Sir/Ma'am, my project is a Customer Support AI Chatbot Agent developed using Python and Streamlit. It automates common customer-support queries using a structured FAQ knowledge base and keyword-based natural language processing. The system provides a fallback response when it cannot identify a query, and the architecture can later be extended with an LLM API and database."

## Important

Current version intentionally uses a local FAQ/keyword engine, so it can run without an API key. An AI/LLM integration can be added as the next version.
