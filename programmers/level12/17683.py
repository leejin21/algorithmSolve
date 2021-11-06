# 방금 그곡
'''
방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다.
네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
각 음은 1분에 1개씩 재생된다. 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
음악이 00:00를 넘겨서까지 재생되는 일은 없다.
조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.

주의사항
1. C#과 C를 구분해야 함
2. 
    (1) 기억한 멜로디는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디일 수 있음.
        -> 멜로디 1개 = 1분, 반복횟수 = 재생시간/멜로디길이
    (2) m은 musicinfo의 멜로디의 부분집합이어야 함(반드시)
3. 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
4. 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.
5. OUTPUT은 음악제목
'''

def replaceSharp(m):
    return m.replace("C#", "1").replace("D#", "2").replace("F#", "3").replace("G#", "4").replace("A#", "5")

def generateFullMusic(run_time, melody):
    melody = replaceSharp(melody)
    rotate_num = run_time//len(melody)
    remain_time = run_time%len(melody)
    return melody*rotate_num+melody[:remain_time]

def solution(m, musicinfos):
    m = replaceSharp(m)
    answer = ('(None)', 0)
    for mi in musicinfos:
        stt, end, title, melody = mi.split(',')
        stt_hour, stt_min = stt.split(':'); end_hour, end_min = end.split(':')
        run_time = (int(end_hour) - int(stt_hour))*60 + int(end_min) - int(stt_min)
        full_melody = generateFullMusic(run_time, melody)
        # print(stt, end, title, melody, run_time)
        if m in full_melody and run_time > answer[1]:
            answer = (title, run_time)

    return answer[0]

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("A#C", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))