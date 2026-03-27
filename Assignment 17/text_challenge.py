import re

# -------------------------------
# Sample Messy Sentences (20)
# -------------------------------
sentences = [
    "hey broooo!!! 😂 what's up???",
    "I loooove this sooo much!!! ❤️",
    "u coming tmrw?",
    "This is amazng!!!",
    "lol that was funny 😂😂",
    "gud mrng frnd!",
    "cant w8 for the party 🎉",
    "omg this is crazzzyyy",
    "pls send the doc asap",
    "thx for ur help 😊",
    "heyyy wassup??",
    "idk what to do 😭",
    "this is sooo coool!!!",
    "c u later",
    "hru doing?",
    "wowww that's gr8!",
    "im sooo tired 😴",
    "lmao that joke 😂",
    "bday party was littt 🔥",
    "okkkk done 👍"
]

# -------------------------------
# Slang Dictionary
# -------------------------------
slang_dict = {
    "u": "you",
    "tmrw": "tomorrow",
    "lol": "laughing",
    "omg": "oh my god",
    "pls": "please",
    "thx": "thanks",
    "idk": "I don't know",
    "c": "see",
    "hru": "how are you",
    "gr8": "great",
    "bday": "birthday"
}

# -------------------------------
# Emoji Pattern
# -------------------------------
emoji_pattern = re.compile("["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F1E0-\U0001F1FF"
    "]+", flags=re.UNICODE)

# -------------------------------
# Analyzer Function
# -------------------------------
def analyze_sentence(sentence):
    words = sentence.lower().split()

    slang_found = [word for word in words if word in slang_dict]
    emojis_found = emoji_pattern.findall(sentence)

    # simple typo detection (repeated letters)
    typos = re.findall(r"(.)\1{2,}", sentence)

    print("\nSentence:", sentence)
    print("Slang:", slang_found if slang_found else "None")
    print("Emojis:", emojis_found if emojis_found else "None")
    print("Typos (repeated letters):", typos if typos else "None")

    print("Suggested Preprocessing:")
    print("- Convert to lowercase")
    print("- Remove emojis")
    print("- Replace slang with full words")
    print("- Remove repeated characters")
    print("- Correct spelling")


# -------------------------------
# Run Analysis
# -------------------------------
print("=== TEXT CHALLENGE ANALYZER ===")

for s in sentences:
    analyze_sentence(s)