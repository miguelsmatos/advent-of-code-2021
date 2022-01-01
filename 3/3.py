import numpy as np

FILENAME = "input.txt"

array = []

with open(FILENAME, "r") as fo:
    for line in fo:
        digits = [d for d in line if d.isdigit()]
        if len(digits) == 0:
            continue
        array.append(digits)

a = np.array(array, dtype=int)
most_common = np.sum(a, axis=0) > a.shape[0] / 2
least_common = ~most_common
most_common = most_common.astype(int)
least_common = least_common.astype(int)


gamma_rate = int("".join([f"{m}" for m in most_common]), 2)
epsilon_rate = int("".join([f"{m}" for m in least_common]), 2)

power_consumption = gamma_rate * epsilon_rate

print(f"The power consumption is {power_consumption}; g={gamma_rate}; e={epsilon_rate}")


index = 0
selection_o2 = a.copy()
selection_co2 = a.copy()
for index in range(a.shape[1]):
    if selection_o2.shape[0] != 1:
        most_common = int(np.sum(selection_o2[:, index]) >= selection_o2.shape[0] / 2)
        selection_o2 = selection_o2[selection_o2[:, index] == most_common, :]
    if selection_co2.shape[0] != 1:
        least_common = int(np.sum(selection_co2[:, index]) < selection_co2.shape[0] / 2)
        print(selection_co2)
        print(index, least_common)
        selection_co2 = selection_co2[selection_co2[:, index] == least_common, :]

    if selection_o2.shape[0] == 1 and selection_co2.shape[0] == 1:
        break

selection_o2 = selection_o2.flatten()
selection_co2 = selection_co2.flatten()
print(selection_o2)
print(selection_co2)

o2 = int("".join([str(x) for x in selection_o2]), 2)
co2 = int("".join([str(x) for x in selection_co2]), 2)
life_support = o2 * co2

print(f"Life support index: {life_support}, o2 = {o2}, co2 = {co2}")
