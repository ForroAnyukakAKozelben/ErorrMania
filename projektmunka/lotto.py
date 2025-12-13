import random

def generate_numbers(count=5, min_val=1, max_val=99):
    """Generál count darab véletlenszámot min_val és max_val között."""
    return [random.randint(min_val, max_val) for _ in range(count)]

def get_user_numbers(count=5, min_val=1, max_val=99):
    """Bekéri a felhasználótól count darab számot a megadott tartományban."""
    numbers = []
    for i in range(count):
        while True:
            try:
                num = int(input(f"Kérlek add meg az {i+1}. tippedet ({min_val}-{max_val}): "))
                if min_val <= num <= max_val:
                    numbers.append(num)
                    break
                else:
                    print(f"A számnak {min_val} és {max_val} között kell lennie.")
            except ValueError:
                print("Kérlek egész számot adj meg!")
    return numbers

def calculate_score(win_num, play_num):
    """Megszámolja, hány számot talált el a felhasználó."""
    score = 0
    for num in play_num:
        if win_num.count(num) == 1:
            score += 1
    return score

# ---- Fő program ----
win_num = generate_numbers()
play_num = get_user_numbers()
score = calculate_score(win_num, play_num)

print(f"Lottó számok: {win_num}")
print(f"A te számaid: {play_num}")
print(f"Ennyi számot találtál el: {score}")
