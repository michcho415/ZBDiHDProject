def generate_candidates(prev_freq_itemsets, k):
    candidates = []
    n = len(prev_freq_itemsets)

    for i in range(n):
        for j in range(i + 1, n):
            itemset1 = prev_freq_itemsets[i]
            itemset2 = prev_freq_itemsets[j]

            # Join step
            new_itemset = sorted(list(set(itemset1) | set(itemset2)))

            if len(new_itemset) == k:
                candidates.append(new_itemset)

    return candidates


def prune_candidates(candidates, prev_freq_itemsets):
    pruned_candidates = []

    for candidate in candidates:
        is_valid = True
        subsets = [candidate[:i] + candidate[i + 1:] for i in range(len(candidate))]

        for subset in subsets:
            if subset not in prev_freq_itemsets:
                is_valid = False
                break

        if is_valid:
            pruned_candidates.append(candidate)

    return pruned_candidates


def calculate_support(dataset, itemset):
    count = 0
    for transaction in dataset:
        if all(item in transaction for item in itemset):
            count += 1
    return count / len(dataset)


def apriori_alg(dataset, min_support):
    freq_itemsets = []
    k = 1

    while True:
        if k == 1:
            candidates = set(item for transaction in dataset for item in transaction)
        else:
            candidates = generate_candidates(freq_itemsets[-1], k)

        candidates = prune_candidates(candidates, freq_itemsets)

        freq_itemsets_k = []
        for candidate in candidates:
            support = calculate_support(dataset, candidate)
            if support >= min_support:
                freq_itemsets_k.append(candidate)

        if not freq_itemsets_k:
            break

        freq_itemsets.extend(freq_itemsets_k)
        k += 1

    return freq_itemsets