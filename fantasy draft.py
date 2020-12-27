import random

def draft():
    managers = ["Suchir", "Joshua", "Seth", "Victoria"]
    avg_pos = {"Suchir":0, "Joshua":0, "Seth":0, "Victoria":0}
    for i in range(1,101):
        init_draft = sorted(managers, key=lambda k: random.random())
        for name in managers:
            avg_pos[name] += init_draft.index(name)
    for name in managers:
        avg_pos[name] /= 100
    results = {k: v for k, v in sorted(avg_pos.items(), key=lambda item: item[1])}
    return results

def main():
    print(draft())

if __name__ == "__main__":
    main()