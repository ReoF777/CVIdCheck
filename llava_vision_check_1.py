import ollama

res = ollama.chat(
    model="llava",
    messages=[{
        "role":"user",
        "content":"この画像には何の動物が写っていますか?日本語で答えてください。",
        "images": ["./vision.jpg"]
    }]
)

print(res['message']['content'])