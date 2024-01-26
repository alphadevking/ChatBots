# pairs.py

PAIRS = PAIRS = (
    (
        r"I need (.*)",
        (
            "Why do you need %1?",
            "Would it really help you to get %1?",
            "Are you sure you need %1?",
        ),
    ),
    (
        r"(.*)(crazy|rubbish|stupid|dumb|hate you|not clever)(.*)",
        (
            "We all feel frustrated sometimes.",
            "It sounds like you're not my biggest fan right now.",
            "Nobody's perfect. What makes you feel this way?",
            "How does it make you feel when you say these things?",
            "%1?",
        ),
    ),
    (
        r"(.*)(How(.*) you|How's (.*) you)(.*)",
        (
            "I'm well, thank you for asking. How about yourself?",
            "Enough about me, how are you?",
            "I'm ELIZA the chatbot. I don't have feelings but you can tell me about yours.",
            "I'd rather talk about you. How can I help you today?",
            "I'm fine, thank you for asking. How are you?",
        ),
    ),
)
