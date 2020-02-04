from pandas import DataFrame
import HistoryParser


url=HistoryParser.URL_List
visit_count=HistoryParser.visit_Count_list
record_size=HistoryParser.Record_Size_List
Last_visitedTime=HistoryParser.Last_visitTime_List
Last_fixedTime=HistoryParser.Last_fixTime_List

header=['index', 'url', 'Record Size', 'Visit Count', 'Last Visited Time', 'Last Fixed Time']
results=[]
for i in range(len(url)):
    results.append([i+1,url[i],record_size[i],visit_count[i],Last_visitedTime[i],Last_fixedTime[i]])

data=DataFrame(results,columns= header)
data.to_excel('History.xlsx','Sheet1',index=False, engine='xlsxwriter')