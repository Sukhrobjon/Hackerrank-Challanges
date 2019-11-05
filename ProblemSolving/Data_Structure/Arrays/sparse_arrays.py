from collections import Counter
def matching_strings(strings, queries):
    results = []
    string_counter = Counter(strings)

    for word in queries:
        if word in string_counter:
            results.append(string_counter[word])
        else:
            results.append(0)

    return results

strings = ["ab", "ab", "abc"]
queries = ["ab", "abc", "bc"]
result = matching_strings(strings, queries)
print(result)

