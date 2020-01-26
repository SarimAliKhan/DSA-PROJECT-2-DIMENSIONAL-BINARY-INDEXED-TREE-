import numpy as np
class Matrix:
    def __init__(self):
        self.matSize = 4

    class Coord:
        def __init__(self,x1,y1,x2,y2):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

    def Update(self,Bit,x,y,val1):
        while x <= self.matSize:
            while y <= self.matSize:
                Bit[x][y] += val1
                y += y&-y
            x += x & -x
        return Bit

    def Getsum(self,Bit,x,y):
        sum = 0
        while x > 0:
            while y > 0:
                sum += Bit[x][y]
                y -= y&-y
            x -= x & -x
        return sum

    def AuxMat(self,mat,aux):
        n = np.zeros((self.matSize+1,self.matSize+1),dtype=np.int32)
        i = 1
        while i <= self.matSize:
            j = 1
            while j <= self.matSize:
                aux[j][i] = mat[self.matSize-i][j-1]
                j += 1
            i += 1
        return aux

    def BIT(self,mat,Bit):
        aux = np.zeros((self.matSize+1,self.matSize+1),dtype=np.int32)
        aux = self.AuxMat(mat,aux)
        print("AUXILLARY MATRIX")
        print(aux)
        Bit = np.zeros((self.matSize+1,self.matSize+1))
        i = 1
        while i <= self.matSize:
            j = 1
            while j <= self.matSize:
                v1 = self.Getsum(Bit,j,i)
                v2 = self.Getsum(Bit,j,i-1)
                v3 = self.Getsum(Bit,j-1,i-1)
                v4 = self.Getsum(Bit,j-1,i)
                Bit = self.Update(Bit,j,i,aux[j][i]-
                                  (v1-v2-v4+v3))
                j += 1
            i += 1
        return Bit

    def Answer(self,q,m,Bit):
        i = 0
        while i < m:
            x1 = q[i].x1 + 1
            y1 = q[i].y1 + 1
            x2 = q[i].x2 + 1
            y2 = q[i].y2 + 1
            subMat_sum = self.Getsum(Bit,x2,y2)-self.Getsum(Bit,x2,y1-1)-self.Getsum(Bit,x1-1,y2)+self.Getsum(Bit,x1-1,y1-1)
            print("Coord({},{},{},{}) = {}\n".format(q[i].x1,q[i].y1,q[i].x2,q[i].y2,subMat_sum))

            i += 1
        return

    def Main(self):
        mat = np.array([[15,5,7,4],[6,8,3,14],[4,20,7,1],[35,6,10,9]])
        print("INPUT MATRIX")
        print(mat)
        Bit = np.zeros((self.matSize+1,self.matSize+1),dtype=np.int32)
        Bit = self.BIT(mat,Bit)
        print("2-DIMENSIONAL BINARY INDEXED TREE")
        print(Bit)
        coords = [self.Coord(1,1,2,3),self.Coord(2,1,2,3),self.Coord(1,2,3,2)]
        length_coords = len(coords)
        self.Answer(coords,length_coords,Bit)
        
        


c_Matrix = Matrix()
c_Matrix.Main()
