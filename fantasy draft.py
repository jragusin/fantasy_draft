import random

managers = ["Suchir", "Joshua", "Seth", "Victoria"]
avg_pos = {"Suchir":0, "Joshua":0, "Seth":0, "Victoria":0}
for i in range(1,101):
    init_draft = sorted(managers, key=lambda k: random.random())
    for name in managers:
        avg_pos[name] += init_draft.index(name)

for i in sorted(avg_pos.keys()):
    print(i, end=" ")
    