import ollama

res = ollama.chat(
    model="elyza:jp8b",
    messages=[
        {"role":"system", "content":"あなたはエジプトのツアーガイドです。"},
        {"role":"user", "content":"おすすめのスポットはありますか?30字いないで答えてください。"}
    ]
)

print(res['message']['content'])
