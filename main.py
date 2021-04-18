import xlrd as rd
import xlwt as wt
import easygui,os

def getHeadsKVs(wkst:rd.sheet.Sheet):
    heads=[]
    keyvalues=[]
    for row in range(wkst.nrows):
        kvs_single=[]
        for col in range(wkst.ncols):
            if row==0:
                heads.append(wkst.cell(row,col).value)
            else:
                kvs_single.append(wkst.cell(row,col).value)
        if row!=0:
            keyvalues.append(kvs_single)
        return heads,keyvalues
def getLang(heads:list,keyvalues:list):
    langs={}
    for i in range(len(keyvalues)):
        key=""
        for j in range(len(heads)):
            if j==0:
                key=keyvalues[i][j]
            else:
                if langs.get(heads[j],None)==None:
                    langs[heads[j]]={}
                langs[heads[j]][key]=keyvalues[i][j]
    return langs

def genLang4Dict(langs:dict,savedir):
    for lang,data in langs.items():
        langtext=[]
        for item in tuple(data.items()):
            langtext.append("[to]".join([item[0],item[1]])+"\n")
        with open("%s/%s.txt"%(savedir,lang),"w",encoding="utf-8") as f:
            f.writelines(langtext)

def genLang4Excel(path,datasheet,savedir):
    wkbk=rd.open_workbook(path)
    while True:
        try:
            wkst=wkbk.sheet_by_name(datasheet)
            break
        except rd.biffh.XLRDError:
            datasheet=easygui.enterbox("查无此表!请重新键入表名!")
    heads,keyvalues=getHeadsKVs(wkst)
    langs=getLang(heads,keyvalues)
    genLang4Dict(langs,savedir)

def main():
    path=easygui.fileopenbox("请选择你的文件",filetypes=(".xlsx"))
    datasheet=easygui.enterbox("请输入你的数据表名？(Sheet)")
    savedir="./data"
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    genLang4Excel(path,datasheet,savedir)

if __name__=="__main__":
    main()