# Today’s Post 🗓️

A conversational AI-powered Python application that generates
daily Instagram-ready quotes and cinematic visual prompts
on simple user input.

> You type: **“today’s post”**  
> It delivers: **quote, caption, and optional AI-generated visual**

---

## ✨ Features

- Conversational CLI interface
- Daily quote selection from extensible dataset
- Prompt-engineered cinematic image generation
- Automatic date-wise output storage
- Graceful fallback to text-only mode when image generation fails
- Single-file, clean Python implementation

---

## 🧠 How It Works

1. User enters a natural-language command
2. System selects a quote + style for the day
3. Builds a cinematic visual prompt
4. Generates:
   - Quote text
   - Caption
   - (Optional) AI image
5. Saves everything in a date-based folder

---

## 📁 Output Structure

```text
output/
└── YYYY-MM-DD/
    ├── post.txt
    ├── caption.txt
    ├── prompt.txt
    └── image.png   (if enabled)
