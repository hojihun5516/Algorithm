def solution(genres, plays):
    answer = []
    items={}
    SEPARATOR="_"
    genre_count = {g: 0 for g in genres}
    used_genre = {g: 0 for g in genres}
    
    for i,genre,play in zip(range(len(genres)),genres, plays):
        items[genre + SEPARATOR + str(i)] = [i,play,genre]
        genre_count[genre] += play

    genre_count=sorted(genre_count.items(), key = lambda x: x[1], reverse=True)
    
    items=sorted(items.items(), key = lambda x: x[1][1], reverse=True)
    for genre, count in genre_count:
        for k,v in items:
            if k.split(SEPARATOR)[0] == genre and used_genre[genre]!=2:
                answer.append(v[0])
                used_genre[genre]+=1
                
    return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/42579