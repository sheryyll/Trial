import random

print("🔮 Welcome to the Magical Fortune Teller! 🔮")
input("Ask your question and press Enter to reveal your fate... ")

fortunes = [
    "You will have an amazing day! 🌞",
    "A surprise is waiting for you around the corner 🎁",
    "Good news will come from someone unexpected 📬",
    "You’ll achieve something you’ve been dreaming about 🌟",
    "Take a break today — you deserve it ☕",
    "Someone will compliment your smile today 😊",
    "Luck is on your side — take that chance 🍀",
    "Your hard work will soon pay off 💪",
]

print("🪄 Your fortune: " + random.choice(fortunes))
