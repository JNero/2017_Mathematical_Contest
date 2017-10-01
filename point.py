class point(object):
    def __init__(self):
        x=0 #x坐标
        y=0 #y坐标
        self.name=''
        self.count=0  #计数
        self.is_visit = 0 #是否被访问过
        self.is_conflict=0

        self.type=-1  #是什么类型
        '''
        D 出发点0
        Z 装载点1 
        F 发射点2
        J 双向交叉点3
        单向交叉点 4
        '''





