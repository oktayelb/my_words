# 🗂️ Word Dictionary CLI

A simple command-line tool for building and managing your own word dictionary — in **any language**. Add words, define them, search, delete, and even quiz yourself with random entries. Everything is stored locally in a text file you can easily back up or share.

---

## 💡 What It Does

This program lets you:

- ➕ Add words to your personal dictionary
- 📝 Add or update definitions
- 🔍 Search for existing words
- ❌ Delete entries
- 🎲 Display random words (great for practice or learning)
- 🗃️ Automatically sort everything alphabetically — with custom character handling

All data is saved to a simple `words.txt` file in the project directory. No external databases or dependencies.

---

## 🧠 Smart Alphabetical Sorting

By default, Python’s sort won't work well for special characters or non-English alphabets. This tool includes a custom sort function that lets you define the order of characters (e.g., for Turkish, German, Spanish, etc.). You can easily tweak the sort logic to match your language of choice.

__________________________________________________________________________________________________
This is the commands that you can use. Entering " "  (a space) will jump you back to the main menu.
```
Commands:

a - add word
d - define word
s - search word
e - delete word
g - random word
q - quit
```
