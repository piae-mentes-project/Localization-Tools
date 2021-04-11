import xlrd as rd
import xlwt as wt
import easygui,os

wkbk=rd.open_workbook(easygui.fileopenbox("请选择你的文件",filetypes=(".xlsx")))
wkst=wkbk.sheet_by_name(wkbk.sheet_names()[0])
heads=[]
keyvalues=[]
langs={}

if not os.path.exists("./data"):
    os.makedirs("./data")

for row in range(wkst.nrows):
    kvs_single=[]
    for col in range(wkst.ncols):
        if row==0:
            heads.append(wkst.cell(row,col).value)
        else:
            kvs_single.append(wkst.cell(row,col).value)
    if row!=0:
        keyvalues.append(kvs_single)
print(heads)
print(keyvalues)

for i in range(len(keyvalues)):
    key=""
    for j in range(len(heads)):
        if j==0:
            key=keyvalues[i][j]
        else:
            if langs.get(heads[j],None)==None:
                langs[heads[j]]={}
            langs[heads[j]][key]=keyvalues[i][j]
for lang,data in langs.items():
    print(lang)
    print(data)
    print("-----------------------")
    langtext=[]
    for item in tuple(data.items()):
        langtext.append("[to]".join([item[0],item[1]])+"\n")
    with open("./data/%s.txt"%lang,"w",encoding="utf-8") as f:
        f.writelines(langtext)
