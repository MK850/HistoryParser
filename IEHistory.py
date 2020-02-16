import getpass
import binascii
import re
from datetime import datetime, timedelta

def main():
    user=getpass.getuser() #경로 지정을 위한 로그인 사용자 명 읽기
    path= open("C:/Users/"+user+"/AppData/Local/Microsoft/Windows/History/History.IE5/index.dat",'rb')
    read=path.read()
    hex=str(binascii.hexlify(read)) #문자형으로 다루기 위한 변환
    path.close()
    #파일 읽어오기위한 바이트 크기 정의
    basic=2 #한 바이트 읽어오기 위한 단위
    byte_4=basic*4 #4바이트 읽어오기
    byte_8=basic*8 #8바이트 읽어오기

    # URL 리스트 함수
    def URL_LIST(URL_text):
        lengh = len(URL_text)
        Slice = []
        for i in range(0, lengh, 2):
            Slice.append(URL_text[i:i + 2])
        charTohex = []
        for i in range(0, len(Slice)):
            charTohex.append(int(Slice[i], 16))
        charToAscii = []
        for i in range(0, len(Slice)):
            charToAscii.append(chr(charTohex[i]))
        URL_list = "".join(charToAscii)
        return URL_list

    # 시간 리스트
    def Time_List(time):
        Time_Big = time
        BigToLittle = []  # 빅엔디안->리틀엔디안
        for i in range(0, len(Time_Big), 2):
            BigToLittle.append(Time_Big[i:i + 2])
        BigToLittle.reverse()
        Time_big = "".join(BigToLittle)

        hex_Time = int(Time_big, 16)
        ns_100 = 10000000  # 100나노초 값
        Second = hex_Time / ns_100

        # datetime 모듈이용해 초를 기존 시간에 더하기
        stand_time = datetime(1601, 1, 1, 00, 00, 00)
        Second_After = stand_time + timedelta(seconds=Second)

        UTC_9 = Second_After + timedelta(hours=9)
        Trimed_Time = UTC_9.strftime('%Y-%m-%d %H:%M:%S')
        return (str(Trimed_Time) + "(+09:00)")

    # 방문 횟수 리스트 함수
    def Visit_list(visit_count):
        Big_visit = visit_count
        visitBigtoLittle = []  # 빅엔디안->리틀엔디안
        for i in range(0, len(Big_visit), 2):
            visitBigtoLittle.append(Big_visit[i:i + 2])
        visitBigtoLittle.reverse()
        Time_big = "".join(visitBigtoLittle)
        list_visit_count = int(Time_big, 16)
        return (list_visit_count)

    # URL 시그니처 찾기
    Find_from = hex  # 헥스 값을 대입
    URL_Sign = "55524c20"
    Start_sign = []
    for i in re.finditer(URL_Sign, Find_from):
        Start_sign.append(i.start())
    Start_sign.sort()

    # URL 끝 찾기
    Default_end = "00"
    End_list = []
    for i in range(len(Start_sign)):
        End_urls = Find_from.find(Default_end, Start_sign[i] + 2 * byte_8 + 176)
        End_list.append(End_urls)
    End_list.sort()

    visit_Count_list = []
    URL_List = []
    Last_fixTime_List = []
    Last_visitTime_List = []
    History = []

    for i in range(len(Start_sign)):
        URL_sign = Start_sign[i]  # URL 시그니쳐 검색
        END_URL = End_list[i]
        last_fix = hex[URL_sign + 2 * byte_4:URL_sign + 2 * byte_8]
        last_visited = hex[URL_sign + 2 * byte_8:URL_sign + 3 * byte_8]
        visit_count = hex[URL_sign + 168:URL_sign + 168 + byte_4]
        url_trimed = hex[URL_sign + 2 * byte_8 + 208:END_URL]

        visit_Count_list.append(Visit_list(visit_count))
        URL_List.append(URL_LIST(url_trimed))
        Last_fixTime_List.append(Time_List(last_fix))
        Last_visitTime_List.append(Time_List(last_visited))

    for i in range(len(Start_sign)):
        History.append([URL_List[i], visit_Count_list[i], Last_fixTime_List[i], Last_visitTime_List[i]])
    return History

IEHistory = main()
