import time
def typing_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
name = input("What's your name, tech warrior? 👩‍💻: ")
topic = input("What tech topic excites you today? 🚀: ")
print("\n" + "="*50)
typing_effect(f"✨ Welcome {name}! ✨")
typing_effect(f"Today, we conquer the world of {topic} together! 🌌")
typing_effect("Remember... you are not average. You are LEGEND. 💎")
print("="*50)
