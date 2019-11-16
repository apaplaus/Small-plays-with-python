#!/usr/bin/env python3
import copy


class Polynomial:

    def __init__(self, *args, **kwargs):
        """ Inicialize polynomial class"""

        # inicialization with named arguments
        if len(args) == 0 and len(kwargs) != 0:
            self.coefs = self.__process_kwargs(kwargs)
        # inicialization with list argument
        elif len(args) == 1 and isinstance(args[0], list):
            self.coefs = args[0]
        # inicialization with variable arguments length
        elif len(args) >= 1:
            self.coefs = list(args)

    def __process_kwargs(self, kwargs: dict):
        """ Process keyword argument to create appropriate list from it"""

        # find maximum power in keys
        max_pow = 0
        for key in kwargs.keys():
            if int(key[1:]) > max_pow:
                max_pow = int(key[1:])
        # construct list of output coefficients
        output_list = []
        for i in range(max_pow + 1):
            if kwargs.get("x{}".format(i)) is not None:
                output_list.append(kwargs["x{}".format(i)])
            else:
                output_list.append(0)
        return output_list

    def __len__(self):
        """ Return number of coefficients of polynom"""

        return len(self.coefs)

    def __str__(self):
        """ Return string representation of polynom"""

        output = ""
        power = len(self.coefs)
        first_run = True
        for coef in self.coefs[::-1]:
            power -= 1
            if coef == 0:
                continue
            # add empty chr to output if we will add something to output
            if not first_run:
                output += " "
            # decide what sign to use
            if coef > 0:
                # if our coefficient isn't first we add '+'
                if not first_run:
                    output += "+ "
            else:
                output += "- "
            # choose if we will or will not print coefficient to output
            coef = abs(coef)
            if coef > 1 or power == 0:
                output += str(coef)
            # don't print 'x' if its '0' power
            if(power > 0):
                output += "x"
                # don't print power if its 1 power
                if(power > 1):
                    output += "^" + str(power)
            first_run = False
        # return 0 if we have all '0' coefficients, else return out string
        if len(output) == 0:
            return "0"
        else:
            return output

    def __eq__(self, other):
        """ Compare string representations of polynoms"""

        if str(self) == str(other):
            return True
        else:
            return False

    def __mul__(self, other):
        """ Multiply two polynoms"""

        if len(self) > 0 and len(other) > 0:
            tmp_obj = Polynomial([])
            tmp_pol_list = []
            # multiply each coefficient of one polynom with
            # every coefficient of another polynom
            for num, item in enumerate(other.coefs):
                tmp_list = []
                for mem in self.coefs:
                    tmp_list.append(mem * item)
                for i in range(num):
                    tmp_list.insert(0, 0)
                # create new polynom from created list
                tmp_pol_list.append(Polynomial(tmp_list))
            # add every polynom to each other to create output polynom
            for pol in tmp_pol_list:
                tmp_obj += pol
            return tmp_obj
        else:
            return self

    def __add__(self, other):
        """ Add one polynom to another"""

        tmp_obj = copy.deepcopy(self)
        # if one polynom smaller then other iterate through smaller
        if len(self) > len(other):
            for num, item in enumerate(other.coefs):
                tmp_obj.coefs[num] += item
        else:
            for num, item in enumerate(other.coefs):
                if num >= len(tmp_obj):
                    tmp_obj.coefs.append(other.coefs[num])
                else:
                    tmp_obj.coefs[num] += other.coefs[num]
        return tmp_obj

    def __pow__(self, other):
        """ Calculate power of polynom with usage of multiply opperation"""

        polinom = copy.deepcopy(self)
        # multiply our polynom to himself as much times as we need
        for i in range(other - 1):
            polinom *= self
        return polinom

    def derivative(self):
        """ Calculate derivative of polynom"""

        tmp_pol = copy.deepcopy(self)
        # delete smallest power of polynom
        tmp_pol.coefs.remove(tmp_pol.coefs[0])
        if(len(tmp_pol) == 0):
            return Polynomial([])
        for pow, item in enumerate(tmp_pol.coefs, 1):
            tmp_pol.coefs[pow - 1] *= pow
        return tmp_pol

    def at_value(self, first, second=None):
        """ Calculate value of polynom in given X, or difference of polynoms"""

        first_out = 0
        second_out = 0
        for pow, num in enumerate(self.coefs):
            first_out += (first**pow) * num
        # use recursion to calculate value of second polynom
        if second is not None:
            second_out = self.at_value(second)
            return second_out - first_out
        return first_out


def test():
    """Test functionality of implemented methods"""

    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()
