import xlrd
import math
from point import point
import csv

def getPointlist():
    point_list = []
    wb = xlrd.open_workbook('1.xls')  # 打开文件
    sh = wb.sheet_by_index(0)  # 第一个表
    nrows = sh.nrows  # 行数
    for i in range(nrows):
        point_list.append(sh.cell_value(i, 0))
    return point_list

def getPoint(pl,name):
    for p in pl:
        if p.name==name:
            return p



def datainput():
    points=[]
    wb = xlrd.open_workbook('1.xls')  # 打开文件
    sh = wb.sheet_by_index(0)  # 第一个表
    nrows = sh.nrows  # 行数
    for i in range(nrows):
        p=point()
        # print(sh.row(i))
        p.name=sh.cell_value(i,0)
        p.x=sh.cell_value(i,1)
        p.y=sh.cell_value(i,2)
        p.type=sh.cell_value(i,3)
        points.append(p)
    return points



def getCoordinate(list,name):
    for l in list:
        if l.name == name:
           return l.x ,l.y
    print(name+'  坐标点没有找到！！！！！！！！！！')
    return 0,0

def getType(list, type):
    type_list=[]
    for l in list:
        if l.type == type:
            type_list.append(l)
    return type_list

def getSingleType(all_points,name):
    for l in all_points:
        if l.name == name:
            return l.type
    print(name + '  坐标点类型没有找到！！！！！！！！！！')
    return None

def getWeight():
# if __name__ == '__main__':
    p=datainput()
    edge=[]
    wb = xlrd.open_workbook('2.xls')  # 打开文件
    sh = wb.sheet_by_index(0)  # 第一个表
    nrows = sh.nrows  # 行数
    for i in range(nrows):
        e=[]
        dis=0
        a=sh.cell_value(i, 0)
        b=sh.cell_value(i, 1)
        x1,y1=getCoordinate(p,a)
        x2,y2=getCoordinate(p,b)
        if x1!=0 and y1!=0 and x2!=0 and y2!=0:
            c=math.pow((x1-x2),2)+math.pow((y1-y2),2)
            dis=math.sqrt(c)
        e.append(a)
        e.append(b)
        e.append(dis)
        edge.append(e)
    return edge
        # for e in edge:
        #     print(e)
    # csvfile = open('distance.csv', 'w')
    # for e in edge:
    #     writer = csv.writer(csvfile,dialect='excel')
    #     writer.writerow(e)
    # csvfile.close()



