from sys import argv

# Check if the user passed the right number of arguments
if len(argv) != 5:
    print("Error. Not enough arguments")
    exit(-1)

# Prepare variables
minsuppc, minconf, input_file, output_file = argv[1:5]
freq_itemsets, cand_itemsets = {}, {}

# Way below is a code snippet that iterates over every line in the input_file and prints it
# You can use it to generate the frequent itemsets. Inside the small.txt file, every line in 
# is organized like this:
# 
# 0 10
# 0 21
# ..
# transaction_id item_id
#
# Since we're doing only F1 itemsets, for every line you iterate in the txt file, just do this:
#
# freq_itemsets[item_id] = freq_itemsets.get(item_id, 0) + 1
#
# Every time the F1 itemset shows up in the transaction, it adds 1 to it in the hash. This keeps
# track of the itemset's frequency.

ifile = open(input_file, "r")
for line in ifile:
    print(line)

