import collections
import getpass
import binascii
import re
from datetime import datetime, timedelta

user=getpass.getuser() #경로 지정을 위한 로그인 사용자 명 읽기
path= open("C:/Users/"+user+"/AppData/Local/Microsoft/Windows/History/History.IE5/index.dat",'rb')
read=path.read()
hex=str(binascii.hexlify(read)) #문자형으로 다루기 위한 변환
path.close()
#파일 읽어오기위한 바이트 크기 정의
basic=2 #한 바이트 읽어오기 위한 단위
byte_4=basic*4 #4바이트 읽어오기
byte_8=basic*8 #8바이트 읽어오기

#헥스를 텍스트로 읽어오는 함수
def READ(URL_text):
 length=len(URL_text)
 Slice=[]
 for i in range(0,length,2):
    Slice.append(URL_text[i:i+2])
 charTohex=[]
 for i in range(0,len(Slice)):
    charTohex.append(int(Slice[i],16))
 charToAscii=[]
 for i in range(0,len(Slice)):
    charToAscii.append(chr(charTohex[i]))
 for i in range(0,len(charToAscii)):
    print(charToAscii[i],end="")
 print()

#URL 리스트 함수
def URL_LIST(URL_text):
 lengh=len(URL_text)
 Slice=[]
 for i in range(0,lengh,2):
    Slice.append(URL_text[i:i+2])
 charTohex=[]
 for i in range(0,len(Slice)):
    charTohex.append(int(Slice[i],16))
 charToAscii=[]
 for i in range(0,len(Slice)):
    charToAscii.append(chr(charTohex[i]))
 URL_list = "".join(charToAscii)
 return URL_list

#레코드 크기 변환 함수
def Record_Size(size_str):
    size_int=int(size_str)
    Size=128*size_int
    print("Record size:",Size)

#레코드 크기 리스트 함수
def Record_Size_list(size_str):
    size_int=int(size_str)
    Size=128*size_int
    return (str(Size)+"byte")

#헥스값 -> 년도날짜시간 변환 함수
def Time(time):
    Time_Big = time
    BigToLittle = []  #빅엔디안->리틀엔디안
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
    print(Trimed_Time, "(+09:00)")

#시간 리스트 만들기 위함
def Time_List(time):
    Time_Big = time
    BigToLittle = []  #빅엔디안->리틀엔디안
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
    return  (str(Trimed_Time)+"(+09:00)")

#방문 횟수 함수
def Visit(visit_count):
    Big_visit= visit_count
    visitBigtoLittle = []  #빅엔디안->리틀엔디안
    for i in range(0, len(Big_visit), 2):
        visitBigtoLittle.append(Big_visit[i:i + 2])
    visitBigtoLittle.reverse()
    Time_big = "".join(visitBigtoLittle)
    hex_Visit_count= int(Time_big, 16)
    print("Visit count:",hex_Visit_count)

#방문 횟수 리스트 함수
def Visit_list(visit_count):
    Big_visit= visit_count
    visitBigtoLittle = []  #빅엔디안->리틀엔디안
    for i in range(0, len(Big_visit), 2):
        visitBigtoLittle.append(Big_visit[i:i + 2])
    visitBigtoLittle.reverse()
    Time_big = "".join(visitBigtoLittle)
    list_visit_count= int(Time_big, 16)
    return (list_visit_count)

#웹 사이트 리스트 함수
def Web_list(urls):

    visit_CoUnt=visit_Count_list

    web_sig_url = []
    file = []
    for i in range(len(urls)):
        if 'http' in urls[i]:  # url 시작이 http, https
            slash = urls[i].split('/')
            if '' in slash:
                blank = slash.index('')
                del (slash[blank])
                web_sig_url.append(slash[1])

        else:
            file.append('files ' * visit_CoUnt[i])

    Website = []
    for i in range(len(web_sig_url)):
        if web_sig_url[i].count('-'):
            hyphen = web_sig_url[i].split('-')
            hyphen_space = " " + hyphen[3]
            Website.append(hyphen_space*visit_CoUnt[i])
        else:
            dot = web_sig_url[i].split('.')
            dot_space = " " + dot[1]
            Website.append(dot_space*visit_CoUnt[i])

    url_data = file + Website
    count = "".join(url_data).split()

    Counter = collections.Counter(count)
    return(Counter)

#URL 시그니처 찾기
Find_from=hex #헥스 값을 대입
URL_Sign="55524c20"
Start_sign=[]
for i in re.finditer(URL_Sign,Find_from):
     Start_sign.append(i.start())
Start_sign.sort()

#URL 끝 찾기
Default_end="100002"

Case1_sign="00de"+Default_end
Case1_List=[]
for i in re.finditer(Case1_sign,Find_from):
    Case1_List.append(i.start())

Case2_sign="00beadde"+Default_end
Case2_List=[]
for i in re.finditer(Case2_sign,Find_from):
    Case2_List.append(i.start())

Case3_sign="00adde"+Default_end
Case3_List=[]
for i in re.finditer(Case3_sign,Find_from):
    Case3_List.append(i.start())

Case4_sign="00"+Default_end
Case4_List=[]
for i in re.finditer(Case4_sign,Find_from):
    Case4_List.append(i.start())

Case_total=Case1_List+Case2_List+Case3_List+Case4_List
Case_total.sort()

#인덱스 값 정리
for i in range(len(Start_sign)-1):
    if Start_sign[i]>Case_total[i]:
        del Case_total[i]

visit_Count_list=[]
URL_List=[]
Record_Size_List=[]
Last_fixTime_List=[]
Last_visitTime_List=[]

for i in range(len(Start_sign)):
    URL_sign=Start_sign[i] #URL 시그니쳐 검색
    END_URL=Case_total[i]
    size_str=hex[URL_sign+byte_4:URL_sign+2*byte_4]
    last_fix=hex[URL_sign+2*byte_4:URL_sign+2*byte_8]
    last_visited=hex[URL_sign+2*byte_8:URL_sign+3*byte_8]
    visit_count=hex[URL_sign+168:URL_sign +168+byte_4]
    url=hex[URL_sign+2*byte_8+176:END_URL]
    url_trimed = hex[URL_sign + 2 * byte_8 + 208:END_URL]

    visit_Count_list.append(Visit_list(visit_count))
    URL_List.append(URL_LIST(url_trimed))
    Record_Size_List.append(Record_Size_list(size_str))
    Last_fixTime_List.append(Time_List(last_fix))
    Last_visitTime_List.append(Time_List(last_visited))

    if __name__ == "__main__":

        # 히스토리 출력

        print()

        print('[', i + 1, '] ', end="")
        READ(url)
        Record_Size(size_str)
        Visit(visit_count)
        print("Last fixed time: ", end="")
        Time(last_fix)
        print("Last visited time: ", end="")
        Time(last_visited)

Counter=(Web_list(URL_List))
web_key = list(Counter.keys())
web_value = list(Counter.values())