from  dataFormat import getPointlist, getWeight, getType, datainput, getPoint

## 表示无穷大
INF_val = 9999
global di
di=0
class Floyd_Path():
    def __init__(self, node, node_map, path_map):
        self.node = node
        self.node_map = node_map
        self.node_length = len(node_map)
        self.path_map = path_map
        self._init_Floyd()
        self.di=0

    def __call__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        return self._format_path()

    def _init_Floyd(self):
        for k in range(self.node_length):
            for i in range(self.node_length):
                for j in range(self.node_length):
                    tmp = self.node_map[i][k] + self.node_map[k][j]
                    if self.node_map[i][j] > tmp:
                        self.node_map[i][j] = tmp
                        self.path_map[i][j] = self.path_map[i][k]

#        print('_init_Floyd is end')

    def _format_path(self):
        global di
        node_list = []
        temp_node = self.from_node
        obj_node = self.to_node
        di=self.node_map[temp_node][obj_node]
        # print("the shortest path is:",self.node_map[temp_node][obj_node])
        node_list.append(self.node[temp_node])
        while True:
            node_list.append(self.node[self.path_map[temp_node][obj_node]])
            temp_node = self.path_map[temp_node][obj_node]
            if temp_node == obj_node:
                break;
        return node_list


def set_node_map(node_map, node, node_list, path_map):
    for i in range(len(node)):
        ## 对角线为0
        node_map[i][i] = 0
    for x, y, val in node_list:
        node_map[node.index(x)][node.index(y)] = node_map[node.index(y)][node.index(x)] = val
        path_map[node.index(x)][node.index(y)] = node.index(y)
        path_map[node.index(y)][node.index(x)] = node.index(x)


# if __name__ == "__main__":
def floyd(node,node_list,start_node,end_node):
    global di
    res=[]
    # node = ['A', 'B', 'C', 'D', 'E', 'F', 'G','M']
    # node_list = [['A', 'F', 9], ('A', 'B', 10), ('A', 'G', 15), ('B', 'F', 2),
    #              ('G', 'F', 3), ('G', 'E', 12), ('G', 'C', 10), ('C', 'E', 1),
    #              ('D', 'E', 7)]

    # node=getPointlist()
    # node_list=getWeight()

    ## node_map[i][j] 存储i到j的最短距离
    node_map = [[INF_val for val in range(len(node))] for val in range(len(node))]
    ## path_map[i][j]=j 表示i到j的最短路径是经过顶点j
    path_map = [[0 for val in range(len(node))] for val in range(len(node))]

    ## set node_map
    set_node_map(node_map, node, node_list, path_map)

    ## select one node to obj node, e.g. A --> D(node[0] --> node[3])
    from_node = node.index(start_node)
    to_node = node.index(end_node)
    Floydpath = Floyd_Path(node, node_map, path_map)
    path = Floydpath(from_node, to_node)
    # print(path)
    res.append(start_node)
    res.append(end_node)
    res.append(path)
    res.append(di)
    return res


if __name__ == '__main__':
    result=[]
    all_points=datainput()
    # print("all_points")
    # print(all_points)
    gpl = getPointlist()  # 所有节点
    #gpl=['D1', 'D2', 'Z01', 'Z02', 'Z03', 'Z04', 'Z05', 'Z06', 'F01', 'F02', 'F03', 'F04', 'F05', 'F06', 'F07', 'F08', 'F09', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24', 'F25', 'F26', 'F27', 'F28', 'F29', 'F30', 'F31', 'F32', 'F33', 'F34', 'F35', 'F36', 'F37', 'F38', 'F39', 'F40', 'F41', 'F42', 'F43', 'F44', 'F45', 'F46', 'F47', 'F48', 'F49', 'F50', 'F51', 'F52', 'F53', 'F54', 'F55', 'F56', 'F57', 'F58', 'F59', 'F60', 'J01', 'J02', 'J03', 'J04', 'J05', 'J06', 'J07', 'J08', 'J09', 'J10', 'J11', 'J12', 'J13', 'J14', 'J15', 'J16', 'J17', 'J18', 'J19', 'J20', 'J21', 'J22', 'J23', 'J24', 'J25', 'J26', 'J27', 'J28', 'J29', 'J30', 'J31', 'J32', 'J33', 'J34', 'J35', 'J36', 'J37', 'J38', 'J39', 'J40', 'J41', 'J42', 'J43', 'J44', 'J45', 'J46', 'J47', 'J48', 'J49', 'J50', 'J51', 'J52', 'J53', 'J54', 'J55', 'J56', 'J57', 'J58', 'J59', 'J60', 'J61', 'J62']
    gw=getWeight()#节点权重关系数组
    #gw=[['D1', 'Z03', 37.20215047547655], ['D1', 'J09', 32.69556544854363], ['D1', 'J10', 24.20743687382041], ['D1', 'J11', 22.561028345356956], ['D2', 'J02', 40.26164427839479], ['D2', 'J03', 21.095023109728988], ['D2', 'J32', 18.681541692269406], ['D2', 'J12', 24.351591323771842], ['Z01', 'J04', 18.788294228055936], ['Z01', 'J50', 18.439088914585774], ['Z01', 'J48', 23.430749027719962], ['Z02', 'J51', 11.661903789690601], ['Z02', 'J52', 17.46424919657298], ['Z02', 'J54', 13.0], ['Z03', 'J52', 17.0], ['Z03', 'J57', 22.090722034374522], ['Z03', 'J61', 26.248809496813376], ['Z03', 'J09', 35.0], ['Z04', 'J37', 14.142135623730951], ['Z04', 'J38', 10.0], ['Z04', 'J07', 15.811388300841896], ['Z05', 'J41', 9.486832980505138], ['Z05', 'J44', 14.317821063276353], ['Z06', 'J16', 26.419689627245813], ['Z06', 'J25', 29.410882339705484], ['Z06', 'J26', 22.20360331117452], ['Z06', 'J28', 28.653097563788805], ['J01', 'J02', 11.180339887498949], ['J02', 'J47', 9.219544457292887], ['J02', 'J03', 29.120439557122072], ['J03', 'J32', 31.78049716414141], ['J03', 'J33', 29.274562336608895], ['J03', 'J48', 18.35755975068582], ['J03', 'J04', 24.839484696748443], ['J04', 'J33', 19.849433241279208], ['J04', 'J50', 22.561028345356956], ['J04', 'J05', 20.8806130178211], ['J05', 'J34', 17.029386365926403], ['J05', 'J49', 11.0], ['J05', 'J06', 32.01562118716424], ['J06', 'J36', 14.317821063276353], ['J06', 'J51', 8.48528137423857], ['J06', 'J07', 26.92582403567252], ['J07', 'J52', 28.635642126552707], ['J07', 'J08', 19.6468827043885], ['J08', 'J42', 29.154759474226502], ['J08', 'J52', 22.135943621178654], ['J08', 'J09', 17.204650534085253], ['J09', 'J45', 29.120439557122072], ['J09', 'J10', 16.15549442140351], ['J10', 'J45', 23.08679276123039], ['J10', 'J11', 20.223748416156685], ['J11', 'J46', 21.470910553583888], ['J12', 'J32', 13.92838827718412], ['J12', 'J13', 23.323807579381203], ['J13', 'J32', 25.019992006393608], ['J13', 'J21', 20.09975124224178], ['J13', 'J14', 16.401219466856727], ['J14', 'J35', 15.0], ['J14', 'J21', 18.027756377319946], ['J14', 'J15', 37.0], ['J15', 'J25', 23.600847442411894], ['J15', 'J37', 14.035668847618199], ['J15', 'J16', 25.612496949731394], ['J16', 'J39', 15.264337522473747], ['J16', 'J17', 29.068883707497267], ['J17', 'J18', 18.867962264113206], ['J18', 'J29', 19.235384061671343], ['J18', 'J41', 11.180339887498949], ['J18', 'J19', 22.627416997969522], ['J19', 'J31', 21.2602916254693], ['J19', 'J43', 12.649110640673518], ['J19', 'J20', 19.4164878389476], ['J20', 'J31', 20.615528128088304], ['J21', 'F01', 8.602325267042627], ['J21', 'F02', 8.54400374531753], ['J21', 'F03', 8.48528137423857], ['J21', 'J22', 20.396078054371138], ['J22', 'F04', 10.295630140987], ['J22', 'F05', 10.295630140987], ['J22', 'F06', 6.324555320336759], ['J22', 'J23', 17.029386365926403], ['J23', 'F07', 7.615773105863909], ['J23', 'J25', 17.46424919657298], ['J23', 'J24', 27.65863337187866], ['J24', 'F08', 11.661903789690601], ['J24', 'F09', 9.219544457292887], ['J24', 'J26', 19.235384061671343], ['J25', 'F10', 16.0312195418814], ['J25', 'F11', 14.035668847618199], ['J26', 'F12', 9.848857801796104], ['J26', 'F13', 12.649110640673518], ['J26', 'J27', 34.438350715445125], ['J27', 'F14', 13.892443989449804], ['J27', 'F15', 7.615773105863909], ['J27', 'F16', 11.40175425099138], ['J27', 'F17', 10.198039027185569], ['J27', 'J28', 25.495097567963924], ['J28', 'F18', 13.038404810405298], ['J28', 'F19', 8.06225774829855], ['J28', 'J30', 20.615528128088304], ['J28', 'J29', 18.384776310850235], ['J29', 'F20', 9.433981132056603], ['J29', 'J30', 20.024984394500787], ['J29', 'J31', 27.018512172212592], ['J30', 'F21', 8.06225774829855], ['J30', 'F22', 10.295630140987], ['J30', 'J31', 18.027756377319946], ['J31', 'F23', 9.055385138137417], ['J32', 'F24', 9.219544457292887], ['J32', 'J33', 17.0], ['J33', 'F25', 10.198039027185569], ['J33', 'J34', 22.360679774997898], ['J34', 'F26', 10.0], ['J34', 'J35', 15.0], ['J34', 'J36', 25.45584412271571], ['J35', 'F27', 9.433981132056603], ['J35', 'F28', 9.433981132056603], ['J36', 'F29', 9.899494936611665], ['J36', 'F30', 9.899494936611665], ['J37', 'F31', 7.211102550927978], ['J37', 'F32', 8.94427190999916], ['J37', 'F33', 11.704699910719626], ['J38', 'F34', 8.602325267042627], ['J38', 'F35', 9.848857801796104], ['J38', 'J42', 28.460498941515414], ['J39', 'F36', 9.848857801796104], ['J39', 'J40', 15.231546211727817], ['J40', 'F37', 12.083045973594572], ['J40', 'F38', 10.295630140987], ['J40', 'F39', 12.649110640673518], ['J40', 'J42', 22.360679774997898], ['J41', 'F40', 10.04987562112089], ['J42', 'J45', 19.849433241279208], ['J43', 'J44', 25.495097567963924], ['J44', 'J45', 22.80350850198276], ['J44', 'J46', 24.596747752497688], ['J44', 'F41', 12.649110640673518], ['J44', 'F42', 9.055385138137417], ['J45', 'J46', 17.0], ['J46', 'F43', 8.54400374531753], ['J47', 'F44', 10.816653826391969], ['J47', 'F45', 12.529964086141668], ['J47', 'J48', 16.1245154965971], ['J48', 'F46', 14.142135623730951], ['J48', 'F47', 12.0], ['J49', 'F48', 11.661903789690601], ['J49', 'F49', 11.313708498984761], ['J49', 'J50', 25.495097567963924], ['J50', 'F50', 13.038404810405298], ['J50', 'J53', 18.110770276274835], ['J53', 'F51', 11.180339887498949], ['J53', 'J55', 15.620499351813308], ['J53', 'J56', 26.68332812825267], ['J53', 'J59', 21.02379604162864], ['J54', 'J55', 19.0], ['J54', 'J57', 10.04987562112089], ['J55', 'J58', 17.72004514666935], ['J55', 'J59', 17.029386365926403], ['J56', 'F52', 10.0], ['J56', 'F53', 11.661903789690601], ['J56', 'J60', 12.083045973594572], ['J57', 'J58', 14.7648230602334], ['J58', 'J59', 18.973665961010276], ['J58', 'J61', 23.430749027719962], ['J59', 'F54', 12.206555615733702], ['J59', 'J62', 24.08318915758459], ['J60', 'F55', 7.810249675906654], ['J60', 'F56', 8.48528137423857], ['J60', 'J62', 23.323807579381203], ['J61', 'F57', 12.36931687685298], ['J61', 'F58', 10.04987562112089], ['J62', 'F59', 13.038404810405298], ['J62', 'F60', 10.44030650891055]]
    el=getType(all_points,2) #拿到所有发射节点
    for e in el:
        re=floyd(gpl,gw,'D1',e.name)
        result.append(re)
    for e in el:
        re = floyd(gpl, gw, 'D2', e.name)
        result.append(re)
    print(result)
