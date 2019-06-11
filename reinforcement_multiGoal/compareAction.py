current_real = open("currentRealMoves.txt", "r")
previous_real = open("previousRealMoves.txt", "r")

current_fake = open("currentFakeMoves.txt", "r")
previous_fake = open("previousFakeMoves.txt", "r")

current_fake1 = open("currentFakeMoves1.txt", "r")
previous_fake1 = open("previousFakeMoves1.txt", "r")


for i in current_real:
    current_real_string = i.strip()

for i in previous_real:
    previous_real_string = i.strip()

for i in current_fake:
    current_fake_string = i.strip()

for i in previous_fake:
    previous_fake_string = i.strip()

for i in current_fake1:
    current_fake_string1 = i.strip()

for i in previous_fake1:
    previous_fake_string1 = i.strip()


def end_condition(previous, current):
    return previous == current


print(end_condition(current_real_string, previous_real_string) and end_condition(current_fake_string, previous_fake_string) and end_condition(current_fake_string1, previous_fake_string1))

current_real.close()
previous_real.close()
current_fake.close()
previous_fake.close()
current_fake1.close()
previous_fake1.close()

