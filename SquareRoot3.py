import math

# refactoring method renaming
def simpleSquareEquation1(aa,bb,cc):
    descrim = math.sqrt(bb**2-4*aa*cc)
    da = 2*aa #I hava argue here what is cheaper create new varibale or calculate multiplication
    return [(-bb+descrim)/da,(-bb-descrim)/da]


# refactoring method renaming
def simpleSquareEquation3(aCoef):
    descrim = math.sqrt(aCoef[1]**2-4*aCoef[0]*aCoef[2])
    da = 2*aCoef[0] #I hava argue here what is cheaper create new varibale or calculate multiplication
    return [(-aCoef[1]+descrim)/da,(-aCoef[1]-descrim)/da]


def squareEquation1(aCoef):
    descrim2 = aCoef[1]**2-4*aCoef[0]*aCoef[2]
    if (descrim2 < 0): return []
    if (aCoef[0]==0): return [-aCoef[2]/aCoef[1]]
    if (math.fabs(aCoef[1]*aCoef[0]/aCoef[2])>10e+7): print("probable error, unpredictable value")
    descrim = math.sqrt(descrim2)
    da = 2*aCoef[0] #I hava argue here what is cheaper create new varibale or calculate multiplication
    return [(-aCoef[1]+descrim)/da,(-aCoef[1]-descrim)/da]




def testEquation(a,b,c,x):
    return a*x**2+b*x+c

def calcCoef(a,X):
    if (a!=0): return [a,-(X[0]+X[1])*a,(X[0]*X[1])*a]
    return [0, X[0],X[1]]



def internalTestFunctionSquareEquation(aa, XX, equationFunction):
    coef = calcCoef(aa, XX)
    print(coef)
    res = equationFunction(coef)
    print(res)
    testresult = testEquation(coef[0], coef[1], coef[2], res[0])
    print(testresult)

def testSquareEquationNegativeDescrim(aa, bb, cc, equationFunction):
    res = equationFunction([aa,bb,cc])
    print(res)



#internalTestFunctionSquareEquation(1,[1,2],simpleSquareEquation3)
#internalTestFunctionSquareEquation(1,[1,2],squareEquation1)
internalTestFunctionSquareEquation(1000.00,[12345678,-0.0000012345678],squareEquation1)

internalTestFunctionSquareEquation(0,[1,1],squareEquation1)

testSquareEquationNegativeDescrim(1, 1, 1, squareEquation1)
