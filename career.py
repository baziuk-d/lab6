def main():
    with open("career.in", "r") as file:
        lines = file.readlines()

    L = int(lines[0].strip())

    experience = []
    for i in range(1, L+1):
        row = [int(x) for x in lines[i].strip().split()]
        experience.append(row)

    total_experience = 0
    for level in range(L-1, -1, -1):
        max_exp_at_level = max(experience[level])
        total_experience += max_exp_at_level
        if level < L-1:
            for i in range(len(experience[level])):
                if experience[level][i] < max_exp_at_level:
                    if level+1 < len(experience):
                        experience[level+1][i] = max(experience[level+1][i], experience[level][i] + experience[level+1][i])

    with open("career.out", "w") as file:
        file.write(str(total_experience))

main()
