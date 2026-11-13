def count_levels(path):
    counts = {"INFO": 0, "WARN": 0, "ERROR": 0}
    with open(path) as f:
        for line in f:
            if line.strip():
                level = line.split()[0]
                if level in counts:
                    counts[level] += 1
    return counts


if __name__ == "__main__":
    print(count_levels("app.log"))
