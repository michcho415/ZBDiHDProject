from itertools import combinations

# Sample transaction dataset
transactions = [
    ["milk", "bread", "sugar"],
    ["bread", "sugar"],
    ["milk", "bread"],
    ["milk", "bread", "sugar", "eggs"],
    ["eggs", "sugar"]
]


# Function to generate candidate itemsets of size k from frequent itemsets of size k-1
def generate_candidates(freq_itemsets, k):
    candidates = []

    for i in range(len(freq_itemsets)):
        for j in range(i + 1, len(freq_itemsets)):
            itemset1 = freq_itemsets[i]
            itemset2 = freq_itemsets[j]

            # Join step: Combine itemsets if the first k-1 items are the same
            if itemset1[:-1] == itemset2[:-1]:
                new_itemset = sorted(list(set(itemset1) | set(itemset2)))

                # Prune step: Check if all (k-1)-subsets are frequent
                is_valid = True
                for subset in combinations(new_itemset, k - 1):
                    if list(subset) not in freq_itemsets:
                        is_valid = False
                        break

                if is_valid:
                    candidates.append(new_itemset)

    return candidates


# Function to calculate the support of an itemset in the dataset
def calculate_support(itemset):
    count = 0
    for transaction in transactions:
        if itemset in transaction:
            count += 1
    return count / len(transactions)


# Function to find frequent itemsets using the Apriori algorithm
def apriori_alg(transactions, min_support):
    frequent_itemsets = []
    k = 1

    while True:
        if k == 1:
            candidates = set(item for transaction in transactions for item in transaction)
        else:
            candidates = generate_candidates(frequent_itemsets, k)

        frequent_itemsets_k = []
        for candidate in candidates:
            support = calculate_support(candidate)
            if support >= min_support:
                frequent_itemsets_k.append(candidate)

        if not frequent_itemsets_k:
            break

        frequent_itemsets.extend(frequent_itemsets_k)
        k += 1

    return frequent_itemsets