class tbody:
    def __init__(self, val):
        self.val = val
        self.mlist = None
        self.merged = False

    def getval(self):
        return self.val

def solution(commands):
    answer = []
    table = []
    for i in range(50):
        table.append([])
        for j in range(50):
            table[i].append(tbody(None))

    for command in commands:
        cmd = command.split()[0]
        params = command.split()[1:]

        if cmd == "UPDATE":
            if len(params) == 3:
                r, c = map(int, params[:-1])
                val = params[-1]

                if table[r - 1][c - 1].merged != True:
                    table[r - 1][c - 1].val = val
                else:
                    for _r, _c in table[r - 1][c - 1].mlist:
                        table[_r - 1][_c - 1].val = val

            elif len(params) == 2:
                val1, val2 = params
                for i in range(50):
                    for j in range(50):
                        if table[i][j].getval() == val1:
                            table[i][j].val = val2
                            if table[i][j].merged :
                                for _r, _c in table[r - 1][c - 1].mlist:
                                    table[_r - 1][_c - 1].val = val2

        elif cmd == "MERGE":
            r1, c1, r2, c2 = map(int, params)
            if r1 == r2 and c1 == c2:
                break

            if table[r1 - 1][c1 - 1].merged == True and table[r2 - 1][c2 - 1].merged == True:

                if table[r1 - 1][c1 - 1] != None:
                    val = table[r1 - 1][c1 - 1].getval()
                else:
                    val = table[r2 - 1][c2 - 1].getval()
                table[r1 - 1][c1 - 1].mlist.extend(table[r2 - 1][c2 - 1].mlist)
                for _r, _c in table[r1 - 1][c1 - 1].mlist:
                    table[_r - 1][_c - 1].val = val
                    table[_r - 1][_c - 1].mlist = table[r1 - 1][c1 - 1].mlist
                    table[_r - 1][_c - 1].merged = True

            elif table[r2 - 1][c2 - 1].merged == True and table[r1 - 1][c1 - 1].merged == False:
                if table[r1 - 1][c1 - 1] != None:
                    val = table[r1 - 1][c1 - 1].getval()
                else:
                    val = table[r2 - 1][c2 - 1].getval()
                table[r2 - 1][c2 - 1].mlist.append([r1, c1])

                for _r, _c in table[r2 - 1][c2 - 1].mlist:
                    table[_r - 1][_c - 1].val = val
                    table[_r - 1][_c - 1].mlist = table[r2 - 1][c2 - 1].mlist
                    table[_r - 1][_c - 1].merged = True

            elif table[r1 - 1][c1 - 1].merged == True and table[r2 - 1][c2 - 1].merged  == False:
                if table[r1 - 1][c1 - 1] != None:
                    val = table[r1 - 1][c1 - 1].getval()
                else:
                    val = table[r2 - 1][c2 - 1].getval()
                table[r1 - 1][c1 - 1].mlist.append([r2, c2])

                for _r, _c in table[r1 - 1][c1 - 1].mlist:
                    table[_r - 1][_c - 1].val = val
                    table[_r - 1][_c - 1].mlist = table[r1 - 1][c1 - 1].mlist
                    table[_r - 1][_c - 1].merged = True

            else:
                if table[r1 - 1][c1 - 1] != None:
                    val = table[r1 - 1][c1 - 1].getval()
                else:
                    val = table[r2 - 1][c2 - 1].getval()
                li = [[r1, c1], [r2, c2]]

                for _r, _c in li:
                    table[_r - 1][_c - 1].val = val
                    table[_r - 1][_c - 1].mlist = li
                    table[_r - 1][_c - 1].merged = True

        elif cmd == "UNMERGE":
            r, c = map(int, params)
            if table[r - 1][c - 1].merged  == False:
                continue

            temp = table[r - 1][c - 1].getval()
            li = table[r - 1][c - 1].mlist

            for _r, _c in li:
                table[_r - 1][_c - 1].mlist = None
                table[_r - 1][_c - 1].val = None
                table[_r - 1][_c - 1].merged = False
            del li
            table[r - 1][c - 1].val = temp
        elif cmd == "PRINT":
            r, c = map(int, params)
            if not table[r - 1][c - 1].getval() == None:
                answer.append(table[r - 1][c - 1].getval())
            else:
                answer.append("EMPTY")

    return answer
