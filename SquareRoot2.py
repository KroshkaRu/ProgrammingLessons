import math

def simple(a,b,c):
    return [(-b+math.sqrt(b**2-4*a*c))/(2*a),(-b-math.sqrt(b**2-4*a*c))/(2*a)]

def simpleOpt1(a,b,c):
    D = math.sqrt(b**2-4*a*c)
    return [(-b+D)/(2*a),(-b-D)/(2*a)]

def simpleOpt2(a,b,c):
    D = math.sqrt(b**2-4*a*c)
    da = 2*a #I hava argue here what is cheaper create new varibale or calculate multiplication
    return [(-b+D)/da,(-b-D)/da]
# refactoring method renaming
def simpleSquareEquation1(aa,bb,cc):
    descrim = math.sqrt(bb**2-4*aa*cc)
    da = 2*aa #I hava argue here what is cheaper create new varibale or calculate multiplication
    return [(-bb+descrim)/da,(-bb-descrim)/da]

# refactoring function signature
def simpleSquareEquation2(coef):
    descrim = math.sqrt(coef[1]**2-4*coef[0]*coef[2])
    da = 2*coef[0] #I hava argue here what is cheaper create new varibale or calculate multiplication
    return [(-coef[1]+descrim)/da,(-coef[1]-descrim)/da]

# refactoring method renaming
def simpleSquareEquation3(aCoef):
    descrim = math.sqrt(aCoef[1]**2-4*aCoef[0]*aCoef[2])
    da = 2*aCoef[0] #I hava argue here what is cheaper create new varibale or calculate multiplication
    return [(-aCoef[1]+descrim)/da,(-aCoef[1]-descrim)/da]

# refactoring method renaming
def simpleSquareEquation4(aCoef):
    aa = aCoef[0]
    bb = aCoef[1]
    cc = aCoef[2]
    return simpleSquareEquation1(aa,bb,cc)

def simplewrong1(a,b,c):
    return [-b+math.sqrt(b**2-4*a*c)/(2*a),-b-math.sqrt(b**2-4*a*c)/(2*a)]

def simplewrong2(a,b,c):
    return [-b+math.sqrt(2*b**2-4*a*c)/(2*a),-b-math.sqrt(2*b**2-4*a*c)/(2*a)]

def testEquation(a,b,c,x):
    return a*x**2+b*x+c

def calcCoef(a,X):
    return [a,-(X[0]+X[1])*a,(X[0]*X[1])*a]

def calcCoefwrong(a,X):
    return [a,-(X[0]+X[1])/a,(X[0]*X[1])/a]


def testSemiManualSimple(a,X):
    coef = calcCoef(a, X)
    print(coef)
    res = simpleSquareEquation1(coef[0], coef[1], coef[2])
    print(res)
    testresult = testEquation(coef[0], coef[1], coef[2], res[0])
    print(testresult)

def testSemiManualSimpleOpt2(a,X):
    coef = calcCoef(a, X)
    print(coef)
    res = simpleOpt2(coef[0], coef[1], coef[2])
    print(res)
    testresult = testEquation(coef[0], coef[1], coef[2], res[0])
    print(testresult)


def testSemiManualSimpleSquareEquation2(a,X):
    coef = calcCoef(a, X)
    print(coef)
    res = simpleSquareEquation2(coef)
    print(res)
    testresult = testEquation(coef[0], coef[1], coef[2], res[0])
    print(testresult)


def testSemiManualSimpleSquareEquation2(a,X):
    coef = calcCoef(a, X)
    print(coef)
    res = simpleSquareEquation2(coef)
    print(res)
    testresult = testEquation(coef[0], coef[1], coef[2], res[0])
    print(testresult)

def internalTestFunctionSquareEquation(aa, XX, equationFunction):
    coef = calcCoef(aa, XX)
    print(coef)
    res = equationFunction(coef)
    print(res)
    testresult = testEquation(coef[0], coef[1], coef[2], res[0])
    print(testresult)



testSemiManualSimple(1000.00,[12345678,-0.0000012345678])
testSemiManualSimple(1000.00,[12345678,-0.12345678])
testSemiManualSimple(2,[1,2])


testSemiManualSimpleOpt2(1,[1,2])
testSemiManualSimpleSquareEquation2(1,[1,2])


internalTestFunctionSquareEquation(1,[1,2],simpleSquareEquation2)
internalTestFunctionSquareEquation(1,[1,2],simpleSquareEquation4)