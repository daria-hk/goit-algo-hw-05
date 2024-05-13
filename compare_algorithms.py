import requests
import timeit

response1 = requests.get("https://drive.google.com/file/d/18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh/view")
text1 = response1.text
response2 = requests.get("https://drive.google.com/file/d/13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ/view")
text2 = response2.text

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return f"Substring not found"

def build_shift_table(pattern):

    table = {}
    length = len(pattern)

    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):

    shift_table = build_shift_table(pattern)
    i = 0  

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  

        if j < 0:
            return i  

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return f"Substring not found"

def polynomial_hash(s, base=256, modulus=101):

    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):

    substring_length = len(substring)
    main_string_length = len(main_string)
    
    base = 256 
    modulus = 101  
    
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    h_multiplier = pow(base, substring_length - 1) % modulus
    
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return  f"Substring not found"

def kmp_search_func():
    kmp_search(text1, substring)

def boyer_moore_search_func():
    boyer_moore_search(text1, substring)

def rabin_karp_search_func():
    rabin_karp_search(text1, substring)

def kmp_search_func_text2():
    kmp_search(text2, substring)

def boyer_moore_search_func_text2():
    boyer_moore_search(text2, substring)

def rabin_karp_search_func_text2():
    rabin_karp_search(text2, substring)

substring = "script"
execution_time_kmp_search = timeit.timeit(kmp_search_func, number=100000)
execution_time_boyer_moore_search = timeit.timeit(boyer_moore_search_func, number=100000)
execution_time_rabin_karp_search = timeit.timeit(rabin_karp_search_func, number=100000)
execution_time_kmp_search_text2 = timeit.timeit(kmp_search_func_text2, number=100000)
execution_time_boyer_moore_search_text2 = timeit.timeit(boyer_moore_search_func_text2, number=100000)
execution_time_rabin_karp_search_text2 = timeit.timeit(rabin_karp_search_func_text2, number=100000)
print(f" execution time for kmp-search in text_1: {execution_time_kmp_search},\n execution time for boyer-moore-search in text_1: {execution_time_boyer_moore_search},\n execution time for rabin-karp-search in text_1: {execution_time_rabin_karp_search}")
print(f" execution time for kmp-search in text_2: {execution_time_kmp_search_text2},\n execution time for boyer-moore-search in text_2: {execution_time_boyer_moore_search_text2},\n execution time for rabin-karp-search in text_2: {execution_time_rabin_karp_search_text2}")
