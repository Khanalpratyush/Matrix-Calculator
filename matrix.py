from copy import copy, deepcopy

class Matrix:
    """Matrix that supports matrix mathematics"""
    def __init__(self,elements):
        self.elements = elements
        self.size = len(elements[0])
        self.columns = [list(i) for i in zip(*self.elements)]   #the columns of matrix using zip
    
    def givesize(self):
        print( str(len(self.elements))+ ' x '+ str(len(self.columns)))
    
    def matrix_view(self):
        string_matrix = [[str(i) for i in rows] for rows in self.elements]
        lens = [max(map(len, col)) for col in zip(*string_matrix)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in string_matrix]
        print ('\n'.join(table))

    def __len__(self):
        """Number of Rows"""
        return len(self.elements)
    def __getitem__(self,j):
        """Indexing starts at 0 for element"""
        if j < self.size:
            return self.elements[0][j]
        elif j >= self.size:
            a = j//self.size  #integer division gives us the index of first dimension of list
            b = j % self.size #this gives us the index of second dimension  
            return self.elements[a][b]
        else:
            raise IndexError('Index is Out of Range')
    def __setitem__(self,j,value):
        if j < self.size:
            self.elements[0][j] = value
        elif j >= self.size:
            a = j//self.size  #integer division gives us the index of first dimension of list
            b = j % self.size #this gives us the index of second dimension  
            self.elements[a][b] = value
        else:
            raise IndexError('Index is outn of range')
    def __add__(self,other):
        if isinstance(other,Matrix):
            if self.size == other.size and len(self.columns) == len(other.columns):
                return Matrix([list(map(sum,zip(i,j))) for i,j in zip(self.elements,other.elements)])
    def __mul__(self,other):
        if isinstance(other,Matrix):
            if len(self.columns) == len(other.elements):
                mainlist = []
                for rowelements in self.elements:
                    minilist = []
                    for columnelements in other.columns:
                        minilist.append(sum(rowelements[j]*columnelements[j] for j in range(len(columnelements))))
                    mainlist.append(minilist)
                return Matrix(mainlist)
    def transpose(self):
        """Returns a transposed version of matrix(to apply direct use transposedirect"""
        return Matrix(self.columns)
    def transposedirect(self):
        """Convert the given matrix to transpose"""
        self.elements,self.columns = self.columns, self.elements
    

              
hello = Matrix([[1,2,3],[4,5,6]])
print(len(hello.elements))
x= hello.transpose()
print(x.elements)
chello = Matrix([[7,8,9,10],[12,11,9,10],[22,32,11,12],[1,2,3,4]])
def reduced_matrix(matrix,row,column):
    copyofmatrix = deepcopy(matrix)
    copyofmatrix.elements.pop(row)
    for i in range(len(copyofmatrix.elements)):
        copyofmatrix.elements[i].pop(column)
    return copyofmatrix
def determinant(self):
    if len(self.elements) == len(self.columns):
        if len(self.elements) == 2:
            simpledetereminants = self.elements[0][0]*self.elements[1][1]-self.elements[1][0]*self.elements[0][1]
            return simpledetereminants
        else:
            determinants = 0 
            for j in range(len(self.columns)):
                cofactor = ((-1)** (0+j))* self.elements[0][j]*determinant(reduced_matrix( self,0,j))
                answer += detereminants
            return determinants 
determinant(chello)
chello.transposedirect()
chello.elements.pop(0)
chello.transposedirect()
chello.matrix_view()
""" print(len(chello.columns))
okay=hello*chello
okay.matrix_view()
"""""" 
chello.elements.pop(0)
x = chello.tran spose()
x.elements.pop(0)


y =x.transpose()
print(y.elements) """





""" chello.elements.pop(0)
chello.transposedirect()
 """""" chello.elements[0] """

