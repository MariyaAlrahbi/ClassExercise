from counter import Counter

def main():
    tally = Counter()
    tally.click()
    tally.click()
    print("Value:" , tally.getValue())

main()