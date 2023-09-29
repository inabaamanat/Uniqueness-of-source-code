import tokenize

#Tokenize the target project:

def tokenize_to_set(filename):
    with tokenize.open(filename) as file:
        tokens = tokenize.generate_tokens(file.readline)

        token_list = []

        for token in tokens:
            token_list.append(token[1])

    return token_list


token_list = tokenize_to_set("second.py")
# print(token_list)

#ngrams the list of tokenize target project
def tokenize_into_2_grams(token_list):
    list_2_grams = []

    for i in range(0, len(token_list), 2):
        list_2_grams.append(token_list[i : i + 2])

    return list_2_grams

print(tokenize_into_2_grams(token_list))


#Tokenize the corpus

#ngrams the list of tokenize corpus

#compare the to find the redundant