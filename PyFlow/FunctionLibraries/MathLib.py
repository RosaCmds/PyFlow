from FunctionLibrary import *
from AGraphCommon import *
import math
from random import randint


class MathLib(FunctionLibraryBase):
    """doc string for MathLib"""
    def __init__(self):
        super(MathLib, self).__init__()

    @staticmethod
    @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def ceil(x=(DataTypes.Float, 0.0)):
        '''Return the ceiling of x as a float, the smallest integer value greater than or equal to x.'''
        return math.ceil(x)

    @staticmethod
    @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def copysignf(x=(DataTypes.Float, 0.0), y=(DataTypes.Float, 0.0)):
        '''Return x with the sign of y. On a platform that supports signed zeros, copysign(1.0, -0.0) returns -1.0.'''
        return math.copysign(x, y)

    @staticmethod
    @annotated(returns=DataTypes.Int, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def copysign(x=(DataTypes.Int, 0), y=(DataTypes.Int, 0)):
        '''Return x with the sign of y. On a platform that supports signed zeros, copysign(1.0, -0.0) returns -1.0.'''
        return math.copysign(x, y)

    @staticmethod
    @annotated(returns=DataTypes.Int, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def factorial(x=(DataTypes.Int, 0), result=(DataTypes.Reference, DataTypes.Bool)):
        '''Return x factorial. Raises ValueError if x is not integral or is negative.'''
        try:
            f = math.factorial(x)
            result.set_data(True)
            return f
        except:
            result.set_data(False)
            return -1

    @staticmethod
    @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def floor(x=(DataTypes.Float, 0.0)):
        '''Sum of two flaots.'''
        return math.floor(x)

    @staticmethod
    @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def fmodf(x=(DataTypes.Float, 0.0), y=(DataTypes.Float, 0.0)):
        '''Return fmod(x, y), as defined by the platform C library.'''
        return math.fmod(x, y)

    @staticmethod
    @annotated(returns=DataTypes.Int, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def fmod(x=(DataTypes.Int, 0), y=(DataTypes.Int, 0)):
        '''Python x % y.'''
        return x % y

    @staticmethod
    @annotated(returns=None, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def frexp(x=(DataTypes.Float, 0.0), m=(DataTypes.Reference, DataTypes.Float), e=(DataTypes.Reference, DataTypes.Int)):
        '''Return the mantissa and exponent of x as the pair (m, e). m is a float and e is an integer such that x == m * 2**e exactly.'''
        t = math.frexp(x)
        m.set_data(t[0])
        e.set_data(t[1])

    @staticmethod
    @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def fsum(arr=(DataTypes.Array, []), result=(DataTypes.Reference, DataTypes.Bool)):
        '''Return an accurate floating point sum of values in the iterable. Avoids loss of precision by tracking multiple intermediate partial sums.'''
        try:
            s = math.fsum([float(i) for i in arr])
            result.set_data(True)
            return s
        except:
            result.set_data(False)
            return 0.0

    @staticmethod
    @annotated(returns=DataTypes.Bool, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def isinf(x=(DataTypes.Float, 0.0)):
        '''Check if the float x is positive or negative infinity.'''
        return math.isinf(x)

    @staticmethod
    @annotated(returns=DataTypes.Bool, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def isnan(x=(DataTypes.Float, 0.0)):
        '''Check if the float x is a NaN (not a number).'''
        return math.isnan(x)

    @staticmethod
    @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def ldexp(x=(DataTypes.Float, 0.0), i=(DataTypes.Int, 0)):
        '''Return x * (2**i). This is essentially the inverse of function frexp().'''
        return math.ldexp(x, i)

    @staticmethod
    @annotated(returns=None, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def modf(x=(DataTypes.Int, 0), f=(DataTypes.Reference, DataTypes.Float), i=(DataTypes.Reference, DataTypes.Int)):
        '''Return the fractional and integer parts of x. Both results carry the sign of x and are floats.'''
        t = math.modf(x)
        f.set_data(t[0])
        i.set_data(t[1])

    @staticmethod
    @annotated(returns=None, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def fmodf(x=(DataTypes.Float, 0), f=(DataTypes.Reference, DataTypes.Float), i=(DataTypes.Reference, DataTypes.Int)):
        '''Return the fractional and integer parts of x. Both results carry the sign of x and are floats.'''
        t = math.modf(x)
        f.set_data(t[0])
        i.set_data(t[1])

    @staticmethod
    @annotated(returns=DataTypes.Int, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Number-theoretic and representation functions', 'Keywords': []})
    def trunc(x=(DataTypes.Float, 0)):
        '''Return the Real value x truncated to an Integral (usually a long integer).'''
        return math.trunc(x)

    @staticmethod
    @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Power and logarithmic functions', 'Keywords': []})
    def exp(x=(DataTypes.Float, 0.0)):
        '''Return e**x.'''
        return math.exp(x)

    @staticmethod
    @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Power and logarithmic functions', 'Keywords': []})
    def expm1(x=(DataTypes.Float, 0.1)):
        '''Return e**x - 1. For small floats x, the subtraction in exp(x) - 1 can result in a significant loss of precision.'''
        return math.expm1(x)

    @staticmethod
    @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Power and logarithmic functions', 'Keywords': []})
    def log(x=(DataTypes.Float, 1.0), base=(DataTypes.Float, math.e), result=(DataTypes.Reference, DataTypes.Bool)):
        '''With one argument, return the natural logarithm of x (to base e).\nWith two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).'''
        try:
            result.set_data(True)
            return math.log(x, base)
        except:
            result.set_data(False)
            return -1

    @staticmethod
    @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Power and logarithmic functions', 'Keywords': []})
    def log1p(x=(DataTypes.Float, 1.0), result=(DataTypes.Reference, DataTypes.Bool)):
        '''Return the natural logarithm of 1+x (base e). The result is calculated in a way which is accurate for x near zero.'''
        try:
            result.set_data(True)
            return math.log1p(x)
        except:
            result.set_data(False)
            return -1

    @staticmethod
    @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Power and logarithmic functions', 'Keywords': []})
    def log10(x=(DataTypes.Float, 1.0), result=(DataTypes.Reference, DataTypes.Bool)):
        '''Return the base-10 logarithm of x. This is usually more accurate than log(x, 10).'''
        try:
            result.set_data(True)
            return math.log10(x)
        except:
            result.set_data(False)
            return -1

    @staticmethod
    @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Power and logarithmic functions', 'Keywords': []})
    def power(x=(DataTypes.Float, 0.0), y=(DataTypes.Float, 0.0), result=(DataTypes.Reference, DataTypes.Bool)):
        '''Return x raised to the power y.'''
        try:
            result.set_data(True)
            return math.pow(x, y)
        except:
            result.set_data(False)
            return -1

    @staticmethod
    @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Power and logarithmic functions', 'Keywords': []})
    def sqrt(x=(DataTypes.Float, 0.0), result=(DataTypes.Reference, DataTypes.Bool)):
        '''Return the square root of x.'''
        try:
            result.set_data(True)
            return math.sqrt(x)
        except:
            result.set_data(False)
            return -1

    @staticmethod
    @annotated(returns=DataTypes.Int, nodeType=NodeTypes.Pure, meta={'Category': 'Math|Bult-in functions', 'Keywords': ['+']})
    def Sum(arr=(DataTypes.Array, []), result=(DataTypes.Reference, DataTypes.Bool)):
        '''Sums start and the items of an iterable from left to right and returns the total.'''
        try:
            s = math.fsum([int(i) for i in arr])
            result.set_data(True)
            return s
        except:
            result.set_data(False)
            return 0

    @staticmethod
    @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Callable, meta={'Category': 'Math', 'Keywords': ['+', 'append']})
    def addf(A=(DataTypes.Float, 0.0), B=(DataTypes.Float, 0.0)):
        '''Sum of two flaots.'''
        return A + B

    @staticmethod
    @annotated(returns=DataTypes.Int, meta={'Category': 'Math', 'Keywords': ['+', 'append']})
    def add(A=(DataTypes.Int, 0), B=(DataTypes.Int, 0)):
        '''Sum of two ints.'''
        return A + B

    @staticmethod
    @annotated(returns=DataTypes.Int, meta={'Category': 'Math', 'Keywords': ['-']})
    def substract(A=(DataTypes.Int, 0), B=(DataTypes.Int, 0)):
        '''Int substraction.'''
        return A - B

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math', 'Keywords': ['-']})
    def substractf(A=(DataTypes.Float, 0), B=(DataTypes.Float, 0)):
        '''Int substraction.'''
        return A - B

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math', 'Keywords': ['/']})
    def divide(A=(DataTypes.Int, 0), B=(DataTypes.Int, 0), result=(DataTypes.Reference, DataTypes.Bool)):
        '''Integer devision.'''
        try:
            d = A / B
            result.set_data(True)
            return d
        except:
            result.set_data(False)
            return -1

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math', 'Keywords': ['/']})
    def dividef(A=(DataTypes.Float, 0.0), B=(DataTypes.Float, 0.0), result=(DataTypes.Reference, DataTypes.Bool)):
        '''Float devision.'''
        try:
            d = A / B
            result.set_data(True)
            return d
        except:
            result.set_data(False)
            return -1

    @staticmethod
    @annotated(returns=DataTypes.Int, meta={'Category': 'Math', 'Keywords': ['*']})
    def mult(A=(DataTypes.Int, 0), B=(DataTypes.Int, 0)):
        '''Integer multiplication.'''
        return A * B

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math', 'Keywords': ['*']})
    def multf(A=(DataTypes.Float, 0.0), B=(DataTypes.Float, 0.0)):
        '''Float multiplication.'''
        return A * B

    @staticmethod
    @annotated(returns=DataTypes.Int, meta={'Category': 'Math|Bult-in functions', 'Keywords': []})
    def absint(inp=(DataTypes.Int, 0)):
        '''Return the absolute value of a number.'''
        return abs(inp)

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math|Bult-in functions', 'Keywords': []})
    def absfloat(inp=(DataTypes.Float, 0.0)):
        '''Return the absolute value of a number.'''
        return abs(inp)

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math|Trigonometry', 'Keywords': []})
    def cos(x=(DataTypes.Float, 0.0)):
        '''Return the cosine of x radians.'''
        return math.cos(x)

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math|Trigonometry', 'Keywords': []})
    def acos(x=(DataTypes.Float, 0.0)):
        '''Return the arc cosine of x, in radians.'''
        return math.acos(x)

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math|Trigonometry', 'Keywords': []})
    def sin(x=(DataTypes.Float, 0.0)):
        '''Return the sine of x radians.'''
        return math.sin(x)

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math|Trigonometry', 'Keywords': []})
    def asin(x=(DataTypes.Float, 0.0)):
        '''Return the arc sine of x, in radians.'''
        return math.asin(x)

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math|Trigonometry', 'Keywords': []})
    def tan(x=(DataTypes.Float, 0.0)):
        '''Return the tangent of x radians.'''
        return math.tan(x)

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math|Trigonometry', 'Keywords': []})
    def atan(x=(DataTypes.Float, 0.0)):
        '''Return the arc tangent of x, in radians.'''
        return math.atan(x)

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math|Trigonometry', 'Keywords': []})
    def atan2(x=(DataTypes.Float, 0.0), y=(DataTypes.Float, 0.0)):
        '''Return atan(y / x), in radians. The result is between -pi and pi.\nThe vector in the plane from the origin to point (x, y) makes this angle with the positive X axis. The point of atan2() is that the signs of both inputs are known to it, so it can compute the correct quadrant for the angle.\nFor example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4.'''
        return math.atan2(x, y)

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math|Trigonometry', 'Keywords': []})
    def hypot(x=(DataTypes.Float, 0.0), y=(DataTypes.Float, 0.0)):
        '''Return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin to point (x, y).'''
        return math.hypot(x, y)

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math|Angular conversion', 'Keywords': []})
    def degtorad(deg=(DataTypes.Float, 0.0)):
        '''Convert angle x from degrees to radians.'''
        return math.radians(deg)

    @staticmethod
    @annotated(returns=DataTypes.Float, meta={'Category': 'Math|Angular conversion', 'Keywords': []})
    def radtodeg(rad=(DataTypes.Float, 0.0)):
        '''Convert angle x from radians to degrees.'''
        return math.degrees(rad)

    @staticmethod
    @annotated(returns=None, nodeType=NodeTypes.Pure, meta={'Category': 'Math|random', 'Keywords': []})
    def randint(start=(DataTypes.Int, 0), end=(DataTypes.Int, 10), Result=(DataTypes.Reference, DataTypes.Int)):
        '''Return a random integer N such that a <= N <= b.'''
        Result.set_data(randint(start, end))
        push(Result)

    # @staticmethod
    # @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Callable, meta={'Category': 'Math', 'Keywords': []})
    # def AddFloatWithResult(A=(DataTypes.Float, 0.0), B=(DataTypes.Float, 0.0), Result=(DataTypes.Reference, DataTypes.Bool)):
    #     Result.set_data(A > B)
    #     return A + B

    # @staticmethod
    # @annotated(returns=DataTypes.Float, nodeType=NodeTypes.Pure, meta={'Category': 'Math', 'Keywords': []})
    # def AddFloatWithResultPure(A=(DataTypes.Float, 0.0), B=(DataTypes.Float, 0.0), Result=(DataTypes.Reference, DataTypes.Bool)):
    #     Result.set_data(A > B)
    #     push(Result)
    #     return A + B
