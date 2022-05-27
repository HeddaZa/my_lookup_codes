import math
import concurrent.futures
from multiprocessing import Pool
import functools

def make_chunks(data, num_chunks):
    chunk_size = math.ceil(len(data) / num_chunks)
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def map_parallel(mapper, data, num_processes):
    chunks = make_chunks(data, num_processes)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(mapper, chunk) for chunk in chunks]
    return [future.result() for future in futures]


def map_reduce(data, num_processes, mapper, reducer):
    chunks = make_chunks(data, num_processes)
    with Pool(num_processes) as pool:
        chunk_results = pool.map(mapper, chunks)
    return functools.reduce(reducer, chunk_results)




####------------------------------------------------------------
values = [1, 4, 5, 2, 7, 21,     \
          31, 41, 3, 40, 5, 14,  \
          9, 32, 12, 18, 1, 30,  \
          6, 19, 23, 35, 12, 13, \
          0, 12, 42, 41, 11, 9]

results = map_parallel(max, values, 5)
####------------------------------------------------------------
chunks = make_chunks(values, 6)
pool = Pool(6)
results = pool.map(max, chunks)
pool.close()
pool.join()
####------------------------------------------------------------
with Pool(6) as pool:
    results = pool.map(max, chunks)
####------------------------------------------------------------
num_processes = 5
chunks = make_chunks(values,num_processes)

with Pool(num_processes) as pool:
    chunk_results = pool.map(max, chunks)
overall_result = functools.reduce(max,values)
####------------------------------------------------------------
max_value = map_reduce(values, 4, max, max)
####------------------------------------------------------------
with open("english_words.txt") as f:
    words = [word.strip() for word in f.readlines()]
    
def map_max_length(words_chunk):
    length = [len(word) for word in words_chunk]
    return max(length)
max_len = map_reduce(words, 4, map_max_length, max)
####------------------------------------------------------------
with open("english_words.txt") as f:
    words = [word.strip() for word in f.readlines()]
    
def map_max_len_str(words_chunk):
    return max(words_chunk, key = len)

def reduce_max_len_str(word1, word2):
    return map_max_len_str([word1, word2])

max_len_str = map_reduce(words, 4, map_max_len_str, reduce_max_len_str)
####------------------------------------------------------------
with open("english_words.txt") as f:
    words = [word.strip() for word in f.readlines()]

target = "pneumonoultramicroscopicsilicovolcanoconiosis"
def map_contains(words_chunk):
    return target in words_chunk

def reduce_contains(contains1, contains2):
    return contains1 or contains2

is_contained = map_reduce(words, 4, map_contains, reduce_contains)
####------------------------------------------------------------
with open("english_words.txt") as f:
    words = [word.strip() for word in f.readlines()]
    
def map_char_count(words_chunk):
    char_freq = {}
    for word in words_chunk:
        for c in word:
            if c not in char_freq:
                char_freq[c] = 0
            char_freq[c] += 1
    return char_freq

def reduce_char_count(freq1,freq2):
    for c in freq2:
        if c in freq1:
            freq1[c] += freq2[c]
        else:
            freq1[c] = freq2[c]
    return freq1

char_freq = map_reduce(words, 4, map_char_count, reduce_char_count)
####------------------------------------------------------------
with open("english_words.txt") as f:
    words = [word.strip() for word in f.readlines()]
    
def map_average(words_chunk):
    sum_words = sum([len(word) for word in words_chunk])
    return sum_words/len(words)

def reduce_average(res1, res2):
    return res1 + res2

average_word_len = map_reduce(words, 4, map_average, reduce_average)
####------------------------------------------------------------
with open("english_words.txt") as f:
    words = [word.strip() for word in f.readlines()]
    
def map_adjacent(words_chunk):
    adj_freq = {}
    for word in words_chunk:
        for w in range(len(word) - 1):
            seq = word[w] + word[w+1]
            if seq not in adj_freq:
                adj_freq[seq] = 0
            adj_freq[seq] += 1
    return adj_freq

def reduce_adjacent(freq1, freq2):
    for seq in freq2:
        if seq in freq1:
            freq1[seq] += freq2[seq]
        else:
            freq1[seq] = freq2[seq]
    return freq1

pair_freq = map_reduce(words, 4, map_adjacent, reduce_adjacent)
unique_pairs = [seq for seq in pair_freq if pair_freq[seq] == 1]
####------------------------------------------------------------