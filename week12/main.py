import os
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import google.generativeai as genai  # ✅ 注意这里的包名是 generativeai，不是 genai

# 加载环境变量
load_dotenv()

# 读取密钥
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("❌ 未找到 GOOGLE_API_KEY，请在 .env 文件中设置。")

# 配置 Gemini
genai.configure(api_key=api_key)

app = FastAPI(title="Gemini FastAPI Demo")

# 允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "✅ Gemini API server running"}

@app.post("/chat")
def chat(prompt: str = Body(..., embed=True)):
    try:
        # ✅ 模型名要写成 "models/gemini-1.5-flash"
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(prompt)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}
