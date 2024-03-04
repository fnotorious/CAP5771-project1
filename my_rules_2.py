from sys import argv
import pandas as pd
from matplotlib import pyplot as plt

# Check if the user passed the right number of arguments
if len(argv) != 5:
    print("Error. Not enough arguments")
    exit(-1)

# Prepare variables
minsuppc, minconf, input_file, output_file = argv[1:5]
minsuppc = int(minsuppc)
minconf = int(minconf)
freq_itemsets, cand_itemsets = {}, {}

# Get candidate itemsets
with open(input_file, "r") as ifile:
    for line in ifile:
        transaction_id, item_id = map(int, line.strip().split())
        cand_itemsets[item_id] = cand_itemsets.get(item_id, 0) + 1

# Function to generate frequent 1-itemsets
def generate_frequent_1_itemsets(cand_itemsets):
    freq_itemsets = {}
    if minsuppc != -1:
        for itemset, support_count in cand_itemsets.items():
            if support_count >= minsuppc:
                freq_itemsets[itemset] = support_count

    return freq_itemsets

freq_itemsets = generate_frequent_1_itemsets(cand_itemsets)
print(freq_itemsets)

def generate_output_files(freq_itemsets, cand_itemsets, minconf, output_file, teamID):
    # Output file 1
    with open(f"{output_file}_items_2.txt", "w") as f:
        for itemset, support_count in freq_itemsets.items():
            f.write(f"{' '.join(map(str, itemset))}|{support_count}\n")

# Output file 2
    if minconf != -1:
        with open(f"{output_file}_rules_2.txt", "w") as f:
            for k, itemsets in cand_itemsets.items():
                for itemset, support_count in itemsets.items():
                    for i in range(1, len(itemset)):
                        for lhs in combinations(itemset, i):
                            rhs = tuple(sorted(set(itemset) - set(lhs)))
                            confidence = support_count / freq_itemsets[lhs]
                            if confidence >= minconf:
                                f.write(f"{' '.join(map(str, lhs))}|{' '.join(map(str, rhs))}|{support_count}|{confidence}\n")


 # Output file 3
    with open(f"{output_file}_info_2.txt", "w") as f:
        f.write(f"minsuppc: {minsuppc}\n")
        f.write(f"minconf: {minconf}\n")
        f.write(f"input file: {input_file}\n")
        f.write(f"output name: {output_file}\n")
        f.write(f"Number of items: {len(freq_itemsets)}\n")
        f.write(f"Number of transactions: ...\n")  # You need to calculate this, not implemented
        f.write(f"The length of the longest transaction: ...\n")  # You need to calculate this,  not implemented
        f.write(f"The length of the largest frequent k-itemset: {max(len(itemset) for itemset in freq_itemsets)}\n")
        f.write(f"Number of frequent 1-itemsets: {len(freq_itemsets)}\n") # not implemented
        f.write(f"Number of frequent 2-itemsets: {len(cand_itemsets[2])}\n") # not implemented
        f.write(f"Number of frequent 𝑘 –itemsets: ...\n")  # not implemented
        f.write(f"Total number of frequent itemsets: {sum(len(itemsets) for itemsets in cand_itemsets.values())}\n")
        f.write(f"Number of high confidence rules: ...\n")  # You need to calculate this, not implemented
        f.write("The rule with the highest confidence: ...\n")  # You need to calculate this, not implemented
        f.write("Time in seconds to find the frequent itemsets: ...\n")  # You need to calculate this, not implemented
        f.write("Time in seconds to find the confident rules: ...\n")  # You need to calculate this, not implemented

#Output 4 
plt.bar(x, height, width, bottom, align) #need more information and what variables will be used 

#Output 5 
plt.bar(x, height, width, bottom, align) #need more information and what variables will be used 
