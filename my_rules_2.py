from sys import argv

# Check if the user passed the right number of arguments
if len(argv) != 5:
    print("Error. Not enough arguments")
    exit(-1)

# Prepare variables
minsuppc, minconf, input_file, output_file = argv[1:5]
freq_itemsets, cand_itemsets = {}, {}

# Function to generate frequent 1-itemsets
def generate_frequent_1_itemsets(input_file):
    freq_itemsets = {}
    with open(input_file, "r") as ifile:
        for line in ifile:
            transaction_id, item_id = map(int, line.strip().split())
            freq_itemsets[item_id] = freq_itemsets.get(item_id, 0) + 1
    return freq_itemsets
