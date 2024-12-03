import ollama

res = ollama.chat(
    model="llava",
    messages=[{
        "role":"user",
        "content":"この画像に写っている人の表情を最大10字以内で日本語で答えてください。理由はいりません。",
        "images": ["./face.jpg"]
    }]
)

print(res['message']['content'])