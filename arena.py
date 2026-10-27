def battle(prompt):
    msgs = [{"role": "user", "content": prompt}]

    # Model A — Google Gemini
    a = google_client.chat.completions.create(model="gemini-3.5-flash-lite", messages=msgs)

    # Model B — Llama on Groq (same code, different brain!)
    b = groq_client.chat.completions.create(model="openai/gpt-oss-120b", messages=msgs)

    return a.choices[0].message.content, b.choices[0].message.content