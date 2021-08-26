import time  # Both this and the next line
import random  # Are for generating random values
import matplotlib.pyplot as plt  # To plot PDFs
from math import log2


def inputMatrix(matrixNo, minimum, maximum):
    r = int(input('\nEnter no. of rows of matrix ' + matrixNo + ': '))
    c = int(input('Enter no. of columns of matrix ' + matrixNo + ': '))

    ch = input(
        '\nEnter values manually (enter \'1\') or randomize (enter \'hit any other character\')?\nMake your choice: ')
    if (ch != '1'):
        m = randomize(r, c, minimum, maximum)
        return m

    print('\nEnter the matrix row by row...')
    m = []
    for i in range(r):
        l = []
        for j in range(c):
            x = int(input('M[' + str(i + 1) + '][' + str(j + 1) + ']:'))
            while x not in range(minimum, maximum):
                print('\nDisallowed value for element! Please enter a value between', minimum, 'and',
                      maximum, '!!')
                x = int(input('M[' + str(i + 1) + '][' + str(j + 1) + ']:'))
            l.append(x)
        m.append(l)
    return m


def plotPDF(m, matrixNo):
     uniqueM = set()

    #Find all the unique elements in the matrix using sets.
     for i in range(len(m)):
         for j in range(len(m[i])):
             uniqueM.add(m[i][j])

     # Convert back to list to make it iterable.
     uniqueM = list(uniqueM)

     # Find the frequency of each element in list.
     freqs = []
     for i in uniqueM:
         ct = 0
         for j in range(len(m)):
             for k in range(len(m[j])):
                 if i == m[j][k]:
                     ct = ct + 1
         freqs.append(ct/(len(m)*len(m[0])))

     plt.bar(uniqueM, freqs)
     plt.xlabel('Values in matrix ' + matrixNo)
     plt.ylabel('Relative frequency of values')
     plt.title('PDF of values in matrix ' + matrixNo)
     plt.show()

def calc(m1, m2):
    uniqueM1 = set()
    uniqueM2 = set()

    # Find all the unique elements in the matrices using sets.
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            uniqueM1.add(m1[i][j])

    for i in range(len(m2)):
        for j in range(len(m2[i])):
            uniqueM2.add(m2[i][j])

    # Convert back to list to make it iterable.
    uniqueM1 = sorted(list(uniqueM1))
    uniqueM2 = sorted(list(uniqueM2))

    # Find the frequency of each element in list.
    freq1 = []
    for i in uniqueM1:
        ct = 0
        for j in range(len(m1)):
            for k in range(len(m1[j])):
                if i == m1[j][k]:
                    ct = ct + 1
        freq1.append(round(ct / (len(m1) * len(m1[0])), 2))

    freq2 = []
    for i in uniqueM2:
        ct = 0
        for j in range(len(m2)):
            for k in range(len(m2[j])):
                if i == m2[j][k]:
                    ct = ct + 1
        freq2.append(round(ct / (len(m2) * len(m2[0])), 2))

    return uniqueM1, freq1, uniqueM2, freq2


def randomize(r, c, mini, maxi):
    random.seed(time.time())
    m = []
    for i in range(r):
        l = []
        for j in range(c):
            l.append(random.randint(mini, maxi))
        m.append(l)
    return m


def findDifferenceBetweenPDFs(x1, Pofx1, x2, Qofx2):
    print(x1, Pofx1, x2, Qofx2)
    for i in x1:
        if i not in x2:
            print('Result: Information Difference is Infinity.')
            return

    sum = 0
    for i in range(len(x1)):
        if x1[i] in x2:
            sum += Pofx1[i] * log2((Pofx1[i] / Qofx2[i]))
    print('Result: Information difference is', sum, 'bits.')


def main():
    print('*************************************************************************************')
    print(' Information Theory Assignment Solution: To find the \'distance\' between two matrices')
    print('*************************************************************************************')
    minimum = int(input('\nEnter the minimum allowed value for the elements of the matrices: '))
    maximum = int(input('Enter the maximum allowed value for the elements of the matrices: '))

    m1 = inputMatrix('1', minimum, maximum)
    m2 = inputMatrix('2', minimum, maximum)

    print('\nInput matrices: \n\nMatrix 1:')
    for l in m1:
        print(l, '\n', end='')

    print('\nMatrix 2:')
    for l in m2:
        print(l, '\n', end='')

    plotPDF(m1, '1')
    plotPDF(m2, '2')
    print('\nPlotting pdfs on a graph... Close the graph window to continue program execution.')
    var1vals, pdf1vals, var2vals, pdf2vals = calc(m1, m2)
    print('\nFinding difference between the pdfs...\n')
    findDifferenceBetweenPDFs(var1vals, pdf1vals, var2vals, pdf2vals)


if __name__ == "__main__":
    main()
