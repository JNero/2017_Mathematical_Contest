import xlrd

from dataFormat import getPointlist, getSingleType, datainput

pernum=[3,3,6]
vehicle={'A':{'F':70,'S':45},'B':{'F':60,'S':35},'C':{'F':50,'S':30}}
'''
:var
'''
def getRoadType(start,end,all_points):
    s=getSingleType(all_points,start)
    e=getSingleType(all_points,end)
    # print("s",s)
    # print("e",e)
    if int(s)==3 and  int(e)==3:
        return 'F'
    else:
        return 'S'

def getSpeed(start,end,vh,all_points):
         ty=getRoadType(start,end,all_points)
         return vehicle.get(vh).get(ty)

def getT(start,end,sp,getweight):
    for gw in getweight:
        if start==gw[0] and end==gw[1]:
            return gw[-1]/sp

def getPerdis():
    perdislist = []
    wb = xlrd.open_workbook('dis.xls')  # 打开文件
    sh = wb.sheet_by_index(0)  # 第一个表
    nrows = sh.nrows  # 行数
    for i in range(nrows):
        p = []
        # print(sh.row(i))
        p.append(sh.cell_value(i, 0))
        p.append(sh.cell_value(i, 1))
        p.append(sh.cell_value(i, 2))
        perdislist.append(p)
    return perdislist

def countTime(all_points,all_weight,all_sites):
    D1_list=[]
    D2_list=[]

    for asite in all_sites:
        if asite[0][0] == 'D1':
            D1_list.append(asite[0])
        elif asite[0][0] == 'D2':
            D2_list.append(asite[0])

    cd=0
    cd2=0

    tml=[]
    tml2=[]
    for d in D1_list:
        a = []
        a.append(d)
        if cd<pernum[2]:
            a = []
            a.append(d)
            a.append('C')
            cd += 1
            tml.append(a)
        elif cd>=pernum[2] and cd <pernum[1]+pernum[2]:
            a = []
            a.append(d)
            a.append('B')
            cd += 1
            tml.append(a)
        else:
            a = []
            a.append(d)
            a.append('A')
            cd += 1
            tml.append(a)

    for d in D2_list:
        a = []
        a.append(d)
        if cd2 < pernum[2]:
            a = []
            a.append(d)
            a.append('C')
            cd2 += 1
            tml2.append(a)
        elif cd2 >= pernum[2] and cd2 < pernum[1] + pernum[2]:
            a = []
            a.append(d)
            a.append('B')
            cd2 += 1
            tml2.append(a)
        else:
            a = []
            a.append(d)
            a.append('A')
            cd += 1
            tml2.append(a)
 #tml2=[[['D2', 'J32', 'J33', 'F25', 'J33', 'J04', 'Z01', 'J50', 'J49', 'F48'], 'C'], [['D2', 'J03', 'J04', 'J50', 'F50', 'J50', 'Z01', 'J50', 'J53', 'F51'], 'C'], [['D2', 'J03', 'J48', 'F47', 'J48', 'Z01', 'J50', 'J53', 'J56', 'F53'], 'C'], [['D2', 'J03', 'J48', 'F46', 'J48', 'Z01', 'J50', 'J53', 'J56', 'F52'], 'C'], [['D2', 'J02', 'J47', 'F44', 'J47', 'J48', 'Z01', 'J50', 'J49', 'F49'], 'C'], [['D2', 'J32', 'J13', 'J21', 'F01', 'J21', 'J14', 'J15', 'J37', 'Z04', 'J37', 'F31'], 'C'], [['D2', 'J32', 'J13', 'J21', 'F02', 'J21', 'J14', 'J15', 'J37', 'Z04', 'J37', 'F32'], 'B'], [['D2', 'J32', 'J13', 'J21', 'F03', 'J21', 'J14', 'J15', 'J37', 'Z04', 'J37', 'F33'], 'B'], [['D2', 'J32', 'J33', 'J34', 'F26', 'J34', 'J36', 'J06', 'J51', 'Z02', 'J51', 'J06', 'J36', 'J34', 'J35', 'F28'], 'B'], [['D2', 'J32', 'F24', 'J32', 'J33', 'J34', 'J36', 'J06', 'J51', 'Z02', 'J54', 'J55', 'J59', 'J62', 'F59'], 'A'], [['D2', 'J32', 'J33', 'J34', 'J35', 'F27', 'J35', 'J34', 'J36', 'J06', 'J51', 'Z02', 'J51', 'J06', 'J36', 'F29'], 'A'], [['D2', 'J02', 'J47', 'F45', 'J47', 'J48', 'Z01', 'J50', 'J53', 'J55', 'J54', 'Z02', 'J51', 'J06', 'J36', 'F30'], 'A']]

    finalTime=[] #
    sum1=0
    for m in tml:
        #m=[['D1', 'J11', 'J46', 'J44', 'F42', 'J44', 'Z05', 'J41', 'J18', 'J29', 'J30', 'F22'], 'C']
        a = []
        b=0
        for i in range(len(m[0])-1):
            v=getSpeed(m[0][i],m[0][i+1],m[-1],all_points)
            # print(m[0][i],"->",m[0][i+1],round(getT(m[0][i],m[0][i+1],v,all_weight)*60,2))
            b+=round(getT(m[0][i], m[0][i + 1], v, all_weight) * 60,2)
            a.append(round(getT(m[0][i],m[0][i+1],v,all_weight)*60,2))
        a.append(round(b,2))
        sum1 += b
        finalTime.append(a)


    #齐射时间
    countQ=[]
    for i in range(len(tml)):
        sss=[]
        qqqq=[]
        # print(tml[i])
        # print(finalTime[i][:-1])
        for tt in range(len(tml[i][0])):
            if tml[i][0][tt][0]=='F':
                qqqq.append(tt)
        sss.append(tml[i])
        sss.append(qqqq[0])
        sss.append(finalTime[i][:-1])
        countQ.append(sss)


    # print(countQ)
    # print(round(sum1,2))

    finalTime2 = []
    sum2 = 0
    qisheshijian2 = 0
    for m in tml2:
        # m=[['D1', 'J11', 'J46', 'J44', 'F42', 'J44', 'Z05', 'J41', 'J18', 'J29', 'J30', 'F22'], 'C']
        a = []
        b = 0
        for i in range(len(m[0]) - 1):
            v = getSpeed(m[0][i], m[0][i + 1], m[-1], all_points)
            # print(m[0][i],"->",m[0][i+1],round(getT(m[0][i],m[0][i+1],v,all_weight)*60,2))
            b += round(getT(m[0][i], m[0][i + 1], v, all_weight),2) * 60

            a.append(round(getT(m[0][i], m[0][i + 1], v, all_weight) * 60,2))

        a.append(round(b, 2))
        sum2 += b
        finalTime2.append(a)

    print("------------------------------------------")

    for i in range(len(tml2)):
        sss = []
        qqqq = []
        # print(tml[i])
        # print(finalTime[i][:-1])
        for tt in range(len(tml2[i][0])):
            if tml2[i][0][tt][0] == 'F':
                qqqq.append(tt)
        sss.append(tml2[i])
        sss.append(qqqq[0])
        sss.append(finalTime2[i][:-1])
        countQ.append(sss)
    print(len(countQ))
    print(countQ)

if __name__ == '__main__':
    des4=[[['D2', 'J32', 'J33', 'F25', 'J33', 'J04', 'Z01', 'J50', 'J49', 'F48'], 150.311437488216], [['D2', 'J03', 'J04', 'J50', 'F50', 'J50', 'Z01', 'J50', 'J53', 'F51'], 160.7416337655903], [['D2', 'J03', 'J48', 'F47', 'J48', 'Z01', 'J50', 'J53', 'J56', 'F53'], 161.77842299693864], [['D2', 'J03', 'J48', 'F46', 'J48', 'Z01', 'J50', 'J53', 'J56', 'F52'], 164.40079045470995], [['D2', 'J02', 'J47', 'F44', 'J47', 'J48', 'Z01', 'J50', 'J49', 'F49'], 165.91765589432316], [['D1', 'J11', 'J46', 'J44', 'F42', 'J44', 'Z05', 'J41', 'J18', 'J29', 'J30', 'F22'], 171.28044945615295], [['D1', 'J11', 'J46', 'J44', 'Z05', 'J41', 'F40', 'J41', 'Z05', 'J41', 'J18', 'J29', 'F20'], 171.35646297969896], [['D1', 'J11', 'J46', 'F43', 'J46', 'J44', 'Z05', 'J41', 'J18', 'J29', 'J28', 'F18'], 171.3602532562809], [['D1', 'J11', 'J46', 'J44', 'F41', 'J44', 'Z05', 'J41', 'J18', 'J29', 'J30', 'F21'], 176.2345280685367], [['D2', 'J32', 'J13', 'J21', 'F01', 'J21', 'J14', 'J15', 'J37', 'Z04', 'J37', 'F31'], 185.5647344983181], [['D2', 'J32', 'J13', 'J21', 'F02', 'J21', 'J14', 'J15', 'J37', 'Z04', 'J37', 'F32'], 187.18126081393905], [['D2', 'J32', 'J13', 'J21', 'F03', 'J21', 'J14', 'J15', 'J37', 'Z04', 'J37', 'F33'], 189.82424407250159], [['D1', 'J09', 'J08', 'J07', 'Z04', 'J38', 'F34', 'J38', 'Z04', 'J37', 'J15', 'J25', 'F10'], 190.373008977587], [['D1', 'J09', 'J08', 'J07', 'Z04', 'J38', 'F35', 'J38', 'Z04', 'J37', 'J15', 'J25', 'F11'], 190.87052335283073], [['D1', 'J10', 'J45', 'J42', 'J40', 'F38', 'J40', 'J39', 'J16', 'Z06', 'J28', 'F19'], 203.72653160683666], [['D1', 'J10', 'J45', 'J42', 'J40', 'F39', 'J40', 'J39', 'J16', 'Z06', 'J26', 'F12'], 203.7705984070929], [['D1', 'J10', 'J45', 'J42', 'J40', 'F37', 'J40', 'J39', 'J16', 'Z06', 'J26', 'F13'], 205.43872191181248], [['D2', 'J32', 'J33', 'J34', 'F26', 'J34', 'J36', 'J06', 'J51', 'Z02', 'J51', 'J06', 'J36', 'J34', 'J35', 'F28'], 211.19625913630182], [['D2', 'J32', 'F24', 'J32', 'J33', 'J34', 'J36', 'J06', 'J51', 'Z02', 'J54', 'J55', 'J59', 'J62', 'F59'], 211.2972518405782], [['D1', 'Z03', 'J61', 'F58', 'J61', 'Z03', 'J57', 'J58', 'J59', 'J62', 'J60', 'F56'], 221.52100987816763], [['D1', 'Z03', 'J57', 'J58', 'J59', 'F54', 'J59', 'J55', 'J54', 'Z02', 'J54', 'J55', 'J59', 'J62', 'F60'], 222.06994940072886], [['D2', 'J32', 'J33', 'J34', 'J35', 'F27', 'J35', 'J34', 'J36', 'J06', 'J51', 'Z02', 'J51', 'J06', 'J36', 'F29'], 222.0789290628362], [['D1', 'Z03', 'J61', 'F57', 'J61', 'Z03', 'J57', 'J58', 'J59', 'J62', 'J60', 'F55'], 225.4848606912999], [['D2', 'J02', 'J47', 'F45', 'J47', 'J48', 'Z01', 'J50', 'J53', 'J55', 'J54', 'Z02', 'J51', 'J06', 'J36', 'F30'], 245.99693905332154]]
    a=datainput()#拿到所有点 以point 数组形式
    b=getPerdis()#得到每个点的距离
    countTime(a,b,des4)





