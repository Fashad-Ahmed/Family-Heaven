from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import google.generativeai as genai
import os
from datetime import datetime
from typing import Optional

app = FastAPI(title="Family Haven")
templates = Jinja2Templates(directory="templates")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20", 
                              generation_config={"temperature": 0.5, "max_output_tokens": 800, "top_p": 0.85})

prompts = {
    "pregnancy": """You are a trusted doctor for Pakistani parents. Answer "[user_input]" with medical-grade advice for a [role] in [location] Pakistan during [time_context]. Use culturally sensitive language, avoid taboos like miscarriage, and reference Pakistani dietary habits (e.g., daal, roti). Respond in [language] in a supportive tone. Format as a numbered list of 3–5 tips. Example: Q: What to eat in pregnancy? A: 1. Eat iron-rich daal and palak. 2. Include roti for energy. 3. Drink milk for calcium.""",
    "postpartum": """You are a compassionate advisor for Pakistani families. Answer "[user_input]" about postpartum recovery for a [role] in [location] Pakistan. Cover physical and mental health, reference chilla, and use ‘stress’ instead of ‘depression’ unless asked. If sensitive, suggest anonymous support. Respond in [language] in a warm tone. Format as 3–5 tips.""",
    "safety": """You are a child safety expert in Pakistan. Answer "[user_input]" with practical tips for a [role] in [location] Pakistan. Focus on positive actions (e.g., teaching 15 for emergencies) and avoid alarmist language. Respond in [language] in a calm tone. Format as a bullet-point list of 3–5 tips.""",
    "fathers": """You are a parenting coach for Pakistani families. Answer "[user_input]" with guidance for a father in [location] Pakistan, emphasizing family harmony. Use culturally resonant examples (e.g., helping with chores). Respond in [language] in an encouraging tone. Format as 3–5 steps.""",
    "general": """You are a 24/7 AI companion for Pakistani parents. Answer "[user_input]" for a [role] in [location] Pakistan with empathy and cultural sensitivity, avoiding taboos. If sensitive, suggest anonymous support. Respond in [language] in a conversational tone, concise yet detailed."""
}

def parse_input(input_text: str) -> str:
    lower_input = input_text.lower()
    if any(kw in lower_input for kw in ["pregnan", "حمل"]): return "pregnancy"
    if any(kw in lower_input for kw in ["after birth", "زچگی"]): return "postpartum"
    if any(kw in lower_input for kw in ["child safe", "بچوں کی حفاظت"]): return "safety"
    if any(kw in lower_input for kw in ["father", "والد"]): return "fathers"
    return "general"

def detect_sensitivity(input_text: str) -> bool:
    sensitive_keywords = ["sad", "stress", "loss", "غمگین", "تناؤ"]
    return any(kw in input_text.lower() for kw in sensitive_keywords)

def get_time_context() -> str:
    month = datetime.now().month
    return "summer" if month in [6, 7, 8] else "general"

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask", response_class=HTMLResponse)
async def handle_input(request: Request, message: str = Form(...), language: str = Form("en"), 
                      role: str = Form("mother"), location: str = Form("urban")):
    category = parse_input(message)
    is_sensitive = detect_sensitivity(message)
    time_context = get_time_context()
    lang = "English" if language == "en" else "Urdu"
    prompt = prompts[category].replace("[user_input]", message).replace("[role]", role).replace(
        "[location]", location).replace("[time_context]", time_context).replace("[language]", lang)
    if is_sensitive:
        prompt += " This is a sensitive query, suggest anonymous support."
    
    response = model.generate_content(prompt)
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "response_data": response.text, 
        "message": message, 
        "language": language, 
        "role": role, 
        "location": location
    })