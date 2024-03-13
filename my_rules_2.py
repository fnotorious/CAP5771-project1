from sys import argv
from itertools import combinations
import matplotlib.pyplot as plt

input_file = 'test/small.txt'

def read_input_file(input_file):
    transactions = {}
    with open(input_file, "r") as file:
        for line in file:
            transaction_id, item_id = map(int, line.strip().split())
            if transaction_id not in transactions:
                transactions[transaction_id] = []
            transactions[transaction_id].append(item_id)
    return transactions

def generate_frequent_itemsets(transactions, minsuppc):
    freq_itemsets = {}
    item_counts = {}
    
    # Count individual item occurrences
    for items in transactions.values():
        for item in items:
            item_counts[item] = item_counts.get(item, 0) + 1

    # Generate frequent 1-itemsets
    freq_itemsets[1] = {frozenset([item]): count for item, count in item_counts.items() if count >= minsuppc}

    k = 2
    while True:
        candidates = set()
        # Generate candidate itemsets of size k
        for itemset1, support1 in freq_itemsets[k-1].items():
            for itemset2, support2 in freq_itemsets[k-1].items():
                if len(itemset1.union(itemset2)) == k:
                    candidates.add(itemset1.union(itemset2))

        # Count support for candidates
        support_counts = {}
        for items in transactions.values():
            for candidate in candidates:
                if candidate.issubset(items):
                    support_counts[candidate] = support_counts.get(candidate, 0) + 1

        # Prune candidates based on minimum support
        freq_itemsets[k] = {itemset: support for itemset, support in support_counts.items() if support >= minsuppc}

        if not freq_itemsets[k]:
            break

        k += 1

    return freq_itemsets

def generate_association_rules(freq_itemsets, minconf):
    association_rules = []
    for k, itemsets in freq_itemsets.items():
        if k < 2:
            continue
        for itemset, support in itemsets.items():
            for i in range(1, k):
                for lhs in combinations(itemset, i):
                    rhs = itemset.difference(lhs)
                    confidence = support / freq_itemsets[len(lhs)][frozenset(lhs)]
                    if confidence >= minconf:
                        association_rules.append((lhs, rhs, support, confidence))
    return association_rules

def write_output_files(freq_itemsets, association_rules, minsuppc, minconf, input_file, output_file):
    with open(f"{output_file}_items_2.txt", "w") as file:
        for k, itemsets in freq_itemsets.items():
            for itemset, support in itemsets.items():
                file.write(f"{' '.join(map(str, itemset))}|{support}\n")

    if minconf != -1:
        with open(f"{output_file}_rules_2.txt", "w") as file:
            for rule in association_rules:
                lhs, rhs, support, confidence = rule
                file.write(f"{' '.join(map(str, lhs))}|{' '.join(map(str, rhs))}|{support}|{confidence}\n")

    with open(f"{output_file}_info_2.txt", "w") as file:
        file.write(f"minsuppc: {minsuppc}\n")
        file.write(f"minconf: {minconf}\n")
        file.write(f"input file: {input_file}\n")
        file.write(f"output name: {output_file}\n")
        file.write(f"Number of items: {len(freq_itemsets[1])}\n")
        file.write(f"Number of transactions: {len(transactions)}\n")
        file.write(f"The length of the longest transaction: {max(len(items) for items in transactions.values())}\n")
        file.write(f"The length of the largest frequent k-itemset: {max(len(itemset) for itemset in freq_itemsets.values())}\n")
        file.write(f"Number of frequent 1-itemsets: {len(freq_itemsets[1])}\n")
        file.write(f"Number of frequent 2-itemsets: {len(freq_itemsets.get(2, []))}\n")
        for k, itemsets in freq_itemsets.items():
            file.write(f"Number of frequent {k}-itemsets: {len(itemsets)}\n")
        file.write(f"Total number of frequent itemsets: {sum(len(itemsets) for itemsets in freq_itemsets.values())}\n")
        if association_rules:
            file.write(f"Number of high confidence rules: {len(association_rules)}\n")
            highest_confidence_rule = max(association_rules, key=lambda x: x[3])
            lhs, rhs, support, confidence = highest_confidence_rule
            file.write(f"The rule with the highest confidence: {' '.join(map(str, lhs))}|{' '.join(map(str, rhs))}|{support}|{confidence}\n")
        else:
            file.write("Number of high confidence rules: 0\n")
            file.write("The rule with the highest confidence: None\n")

def plot_frequent_itemsets(freq_itemsets, minsuppcs, output_file):
    num_frequent_itemsets = [sum(len(itemsets) for itemsets in freq_itemsets.values()) for minsuppc in minsuppcs]
    plt.plot(minsuppcs, num_frequent_itemsets, marker='o')
    plt.title('Number of Frequent Itemsets vs minsuppc')
    plt.xlabel('minsuppc')
    plt.ylabel('Number of Frequent Itemsets')
    plt.grid(True)
    plt.savefig(f"{output_file}_plot_items_2.png")
    plt.show()

# Check if the user passed the right number of arguments
if len(argv) != 5:
    print("Error. Not enough arguments")
    exit(-1)

minsuppc, minconf, input_file, output_file = argv[1:5]

transactions = read_input_file(input_file)
freq_itemsets = generate_frequent_itemsets(transactions, int(minsuppc))
association_rules = generate_association_rules(freq_itemsets, float(minconf))
write_output_files(freq_itemsets, association_rules, int(minsuppc), float(minconf), input_file, output_file)

minsuppcs = [100, 130, 160]
plot_frequent_itemsets(freq_itemsets, minsuppcs, output_file)
