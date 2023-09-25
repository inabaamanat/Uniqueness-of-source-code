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

    for i in range(0, len(token_list), 10):
        list_11granularity.append(token_list[i : i + 10])

    return list_11granularity


granularity_11_list = granularity_11(token_list)
# print(granularity_11_list)
# print(granularity_11_list[1])


def syntactic_redundancy_11(token_list):
    result_list = []
    for lists in token_list:
        for i in range(len(lists) - 1):
            result = 0
            for token1 in lists[i]:
                for token2 in lists[i + 1]:
                    if token1 == token2:
                        result += 1
                    else:
                        result = result
            syntactic_redundancy = result / len(lists[i])
            result_list.append(syntactic_redundancy)

    return result_list


list_syntactic_redundancy = syntactic_redundancy_11(token_list)

print(list_syntactic_redundancy)
