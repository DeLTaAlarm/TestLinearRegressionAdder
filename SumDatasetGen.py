import random as rnd

def generateDataset(length, aMin, aMax, bMin, bMax, name):
    rnd.seed(42)
    datasetLines = ["a, b, c\n"]
    for i in range(length):
        a = rnd.randint(aMin, aMax)
        b = rnd.randint(bMin, bMax)
        c = a + b
        datasetLines.append(f"{a}, {b}, {c}\n")
        if i % 10000 == 0 and i != 0: print(f"{round(i/length*100, 2)}%")

    dataset = "".join(datasetLines)
    with open(name, "w") as f:
        f.write(dataset)


generateDataset(10000, -1000, 1000, -1000, 1000, "datasetBig.csv")


