class tbody :
    def __init__(self, val):
        self.val = val
        self.mbody = None
        self.mlist = list()

    def merged(self):
        if self.mbody == None :
            return False
        else :
            return True

    def getval(self):
        if self.merged():
            return self.mbody
        else :
            return self.val

def solution(commands):
    answer = []
    table = [] # 0~49 / 0~49
    for i in range(50):
        table.append([])
        for j in range(50):
            table[i].append(tbody(None))
    for command in commands :
        # command 와 params 분리
        cmd = command.split()[0]
        params = command.split()[1:]
        # print(cmd, params)

        if cmd == "UPDATE" :
            if len(params) == 3 :
                r, c = map(int, params[:-1])
                val = params[-1]

                #print(r, c, val)
                # "UPDATE r c value"
                if table[r-1][c-1].merged() != True:
                    table[r-1][c-1].val = val
                else :
                    for _r, _c in table[r-1][c-1].mlist:
                        table[_r-1][_c-1].mbody = val
                # (r, c) 위치의 셀을 선택합니다.
                # 선택한 셀의 값을 value로 바꿉니다.
            elif len(params) == 2 :
                val1, val2 = params
                # "UPDATE value1 value2"
                for i in range(50) :
                    for j in range(50):
                        if table[i][j].getval() == val1:
                            if table[i][j].merged() :
                                table[i][j].mbody = val2
                            else:
                                table[i][j].val = val2
                # value1을 값으로 가지고 있는 모든 셀을 선택합니다.
                # 선택한 셀의 값을 value2로 바꿉니다.

        elif cmd == "MERGE":
            r1, c1, r2, c2 = map(int, params)
            if r1 == r2 and c1 == c2 :
                break
            # 선택한 두 위치의 셀이 같은 셀일 경우 무시합니다.
            # 선택한 두 셀은 서로 인접하지 않을 수도 있습니다. 이 경우 (r1, c1) 위치의 셀과 (r2, c2) 위치의 셀만 영향을 받으며, 그 사이에 위치한 셀들은 영향을 받지 않습니다.


            # 두 셀 모두 값을 가지고 있을 경우 병합된 셀은 (r1, c1) 위치의 셀 값을 가지게 됩니다.
            if table[r1-1][c1-1].merged() == True and table[r2-1][c2-1].merged() == True:
                if table[r1-1][c1-1] != None:
                    val = table[r1-1][c1-1].getval()
                else :
                    val = table[r2-1][c2-1].getval()
                table[r1-1][c1-1].mlist.extend(table[r2-1][c2-1].mlist)
                for _r, _c in table[r2-1][c2-1].mlist:
                    table[_r-1][_c-1].mbody = val
                    table[_r-1][_c-1].mlist = table[r1-1][c1-1].mlist
                    # print(table[_r-1][_c-1].mbody, table[_r-1][_c-1].mlist)
            elif table[r2-1][c2-1].merged() == True and table[r1-1][c1-1].merged() == False :
                if table[r1-1][c1-1] != None:
                    val = table[r1-1][c1-1].getval()
                else :
                    val = table[r2-1][c2-1].getval()
                table[r2-1][c2-1].mlist.append([r1, c1])
                # print(table[r2-1][c2-1].mlist)
                for _r, _c in table[r2-1][c2-1].mlist:
                    table[_r-1][_c-1].mbody = val
                    table[_r-1][_c-1].mlist = table[r2-1][c2-1].mlist
                    # print(table[_r-1][_c-1].mbody, table[_r-1][_c-1].mlist)
            elif (table[r1-1][c1-1].merged() == True) and (table[r2-1][c2-1].merged() == False):
                if table[r1-1][c1-1] != None:
                    val = table[r1-1][c1-1].getval()
                else :
                    val = table[r2-1][c2-1].getval()
                table[r1-1][c1-1].mlist.append([r2, c2])
                # print(table[r1-1][c1-1].mlist)
                for _r, _c in table[r1-1][c1-1].mlist:
                    table[_r-1][_c-1].mbody = val
                    table[_r-1][_c-1].mlist = table[r1-1][c1-1].mlist
                    # print(table[_r-1][_c-1].mbody, table[_r-1][_c-1].mlist)
            else :
                if table[r1-1][c1-1] != None :
                    val = table[r1-1][c1-1].getval()
                else :
                    val = table[r2-1][c2-1].getval()
                li = [[r1, c1], [r2, c2]]

                for _r, _c in li:
                    table[_r-1][_c-1].mbody = val
                    table[_r-1][_c-1].mlist = li
                    # print(table[_r-1][_c-1].mbody, table[_r-1][_c-1].mlist)

            # print(table[r1-1][c1-1].getval())
            # print(table[r2-1][c2-1].getval())
            # print(table[r2-1][c2-1].mlist)
        elif cmd == "UNMERGE":
            r, c = map(int, params)
            if table[r-1][c-1].merged() == False:
                continue

            temp = table[r-1][c-1].getval()

            li = table[r-1][c-1].mlist
            # print(li)
            for _r, _c in li :
                table[_r-1][_c-1].mlist = None
                table[_r-1][_c-1].val = None
                table[_r-1][_c-1].mbody = None
                # print(_r, _c)
            del li
            table[r-1][c-1].val = temp
        elif cmd == "PRINT":
            r, c = map(int, params)
            if not table[r-1][c-1].getval() == None:
                answer.append(table[r-1][c-1].getval())
            else:
                answer.append("EMPTY")
        # for i in range(50):
        #     for j in range(50) :
        #         print(table[i][j].getval(), end = ", ")
        #     print()
    return answer

# print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))



# "PRINT r c"
# (r, c) 위치의 셀을 선택하여 셀의 값을 출력합니다.
# 선택한 셀이 비어있을 경우 "EMPTY"를 출력합니다.
