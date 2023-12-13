import itertools

def flat_all_words(words):
    return set().union(*words)
    
def replace_word(word):
    return set(word) - set("antic")

def solution(K, words):
    if K < 5:
        return 0
    
    word_count = K - 5
    replaced_words = list(map(replace_word, words))
    all_words = flat_all_words(replaced_words)

    if len(all_words) <= word_count:
        return len(words)

    combinations = itertools.combinations(all_words, word_count)
    answer = 0

    for comb in combinations:
        comb_set = set(comb)
        count = sum(1 for word in replaced_words if word.issubset(comb_set))
        answer = max(answer, count)

    return answer

# N은 주어지는 문장 수 
# K는 사용가능한 단어 수
N, K = map(int, input().split())
words = [input() for _ in range(N)]

print(solution(K, words))


https://www.acmicpc.net/problem/1062