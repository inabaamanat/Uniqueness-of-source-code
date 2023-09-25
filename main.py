import tokenize


def tokenize_to_set(filename):
    with tokenize.open(filename) as file:
        tokens = tokenize.generate_tokens(file.readline)

        token_list = []

        for token in tokens:
            token_list.append(token[1])

    return token_list


token_list = tokenize_to_set("second.py")
# print(token_list)


def granularity_11(token_list):
    list_11granularity = []

    for i in range(0, len(token_list), 11):
        list_11granularity.append(token_list[i : i + 11])

    return list_11granularity


granularity_11_list = granularity_11(token_list)
# print(granularity_11_list)


def syntactic_redundancy_11(token_list):
    tokens_3_grams = []
    redundant = []

    # Examine each list
    for lists in token_list:
        if len(lists) == 11:
            for i in range(0, 9):
                for j in range(i + 1, 10):
                    for k in range(j + 1, 11):
                        list_3grams = [lists[i], lists[j], lists[k]]
                        tokens_3_grams.append(list_3grams)

    return tokens_3_grams


list_syntactic_redundancy = syntactic_redundancy_11(granularity_11_list)

print(list_syntactic_redundancy)
