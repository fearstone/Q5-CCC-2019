import random
class rule():
    def __init__(self,r1,r2,num):
        self.rin = r1
        self.rout = r2
        self.num = num
        self.typ = len(r2) - len(r1)
        self.parent = ""
    def sub(self,I,pos):
        new = ""
        for i in range(len(I)):
            if i == pos:
                new += self.rout
            elif i < pos or i > pos + len(self.rin)-1:
                new += I[i]
        return new
    def legal(self,I,pos):
        if pos + len(self.rin) > len(I):
            return False
        for i in range(len(self.rin)):
            if I[pos+i] != self.rin[i]:
                return False
        return True

class sup():
    def __init__(self,rul,pos,state,parent):
        self.rul = rul
        self.pos = pos
        self.state = str(state)
        self.parent = parent
    def make(self,lis):
        if self.parent != '':
            lis.append(str(self.rul)+" "+str(self.pos+1)+" "+str(self.state))
            self.parent.make(lis)
        return(lis)

r = input("").split(" ")
r1 = rule(r[0],r[1],1)
r = input("").split(" ")
r2 = rule(r[0],r[1],2)
r = input("").split(" ")
r3 = rule(r[0],r[1],3)


n = input("").split(" ")
I = n[1] #initial
F = n[2] #final

rules = [r1,r2,r3]

op = [sup('','',I,'')] #opened states
cl = [] #closed states
run = True
while run:
    s = op[0] 
    cl.append(s)
    op.remove(s)
    if s.state == F:
        steps = []
        stepp = s.make(steps)
        break
    else:
        for r in rules:
            for x in range(len(s.state)):
                if r.legal(s.state,x): #if move is legal
                    n = sup(r.num,x, r.sub(s.state,x),s) #try move and see if it has been done or not
                    if n in cl: 
                        pass
                    elif not n in op: #if not then put it into the list of states to evaluate
                        op.append(n)

for hey in range(len(stepp)-1,-1,-1): #prints the list of steps to reach state
    print(stepp[hey])

        
    
