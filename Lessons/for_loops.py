"""For loops syntax + practice!"""

pets: list[str] = ["Louie", "Bo", "Bear"]
# tell every pet they're a good boy!
for pet in pets:
    print(f"Good boy, {pet}!")  # "Good boy, " + pet + "!"

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
# print each index: name
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
