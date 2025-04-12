from ALGORITHM_1_LFCO_2025_AT_SS import StringGenerator
from ALGORITHM_2_LFCO_2025_AT_SS import PDA
from ALGORITHM_3_LFCO_2025_AT_SS import Rules_table
import random


# Create instances of the classes
stringGenerator = StringGenerator()
pda = PDA()
rules_table = Rules_table()

# Run the first algorithm

set_of_strings = stringGenerator.generateStrings()

emojis=["🔥", "🌟","💎", "📊", "👨‍💻", "💡", "⌨️", "🖱️", "🥑"]
print("🎲 Generating random strings... 🎲\n")

for idx, s in enumerate(set_of_strings, 1):
    emoji = random.choice(emojis)
    print(f"✨ String {idx}: {emoji}  \"{s}\"")

# Run the second algorithm

print("\n🧠 Checking if the strings are valid... 🧠\n")

results = []

for string in set_of_strings:
    accepted, _ = pda.is_valid(string)

    checkmark = "✅" if accepted else "❌"
    results.append((string, checkmark))

for idx, (s, result) in enumerate(results, 1):
    print(f"{idx}. {s} {result}")

valid_strings , valid_transitions = pda.return_valid_strings(set_of_strings) # Get only the valid strings and their transitions

# Run the third algorithm

print("\n📊 Applying rules... 📊\n")


for i in range(len(valid_strings)):
    
    string = valid_strings[i]
    transitions_done = valid_transitions[i]

    rules_table.aplied_rules(string , transitions_done)
    



