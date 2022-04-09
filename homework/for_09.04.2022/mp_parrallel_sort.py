import multiprocessing as mp
import random
from lesson5 import merge, merge_sort

def merge_seq_of_two_lists(seq):
    return merge(seq[0], seq[1])

def gen_list():
    return [random.randint(-1000000000, 1000000000) for _ in range(1000000)] # 10^6 elements in range [-10^9; 10^9]

def part_list(lst, n):
    part_len = len(lst) // n
    res = []
    for i in range(n-1):
        res.append(lst[part_len * i : part_len * (i+1)])
    res.append(lst[part_len * (n-1):])
    return res

def main():
    lst = gen_list()
    cpu = mp.cpu_count()
    parts = part_list(lst, cpu)

    with mp.Pool(processes = cpu) as pool:
        sorted_parts = pool.map(merge_sort, parts)
    
    while len(sorted_parts) > 1:
        part_count = len(sorted_parts)
        with mp.Pool(processes = part_count // 2) as pool:
            sorted_parts = pool.map(merge_seq_of_two_lists, (sorted_parts[i:i+2] for i in range(part_count // 2)))
        
    return sorted_parts[0]

if __name__ == "__main__":
    print(main()[:20]) # чисто для ДЕМОНстрации