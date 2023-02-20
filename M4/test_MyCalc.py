from MyCalc import MyCalc
import pytest


"""bag27:2/20/2023
Holds test data in a dict. a=first operand, b=second operand, r=output, "true" determines 
if test is supposed to be correct or incorrect. Dict is traversed and depending on "true",
test is asserted to be equal to r or not equal.
"""
def test_add():
    calc = MyCalc()

    data = [{
        "a":"5",
        "b":"5",
        "r":"10",
        "true": True
    },
    {
        "a":"-5",
        "b":"5",
        "r":"0",
        "true": True
    },
    {
        "a":"3",
        "b":"3",
        "r":"-6",
        "true": False
    },
    {
        "a":"-5",
        "b":"0",
        "r":"10",
        "true": False
    },
    {
        "a":"5",
        "b":"-5",
        "r":"0",
        "true": True
    }]

    for d in data:
        if d["true"]:
            assert calc.add(d["a"], d["b"]) == int(d["r"])
        else:
            assert calc.add(d["a"], d["b"]) != int(d["r"])

"""bag27:2/20/2023
Holds test data in a dict. a=first operand, b=second operand, r=output, "true" determines 
if subtraction test is supposed to be correct or incorrect. Dict is traversed and depending on "true",
subraction test is asserted to be equal to r or not equal."""
def test_sub():
    calc = MyCalc()

    data = [{
        "a":"5",
        "b":"5",
        "r":"0",
        "true": True
    },
    {
        "a":"-5",
        "b":"5",
        "r":"-10",
        "true": True
    },
    {
        "a":"3",
        "b":"3",
        "r":"6",
        "true": False
    },
    {
        "a":"-5",
        "b":"0",
        "r":"5",
        "true": False
    },
    {
        "a":"5",
        "b":"-5",
        "r":"10",
        "true": True
    }]

    for d in data:
        if d["true"]:
            assert calc.sub(d["a"], d["b"]) == int(d["r"])
        else:
            assert calc.sub(d["a"], d["b"]) != int(d["r"])

"""bag27:2/20/2023
Holds test data in a dict. a=first operand, b=second operand, r=output, "true" determines 
if multiplication test is supposed to be correct or incorrect. Dict is traversed and depending on "true",
multiplication test is asserted to be equal to r or not equal."""
def test_mult():
    calc = MyCalc()

    data = [{
        "a":"5",
        "b":"5",
        "r":"25",
        "true": True
    },
    {
        "a":"-5",
        "b":"5",
        "r":"-25",
        "true": True
    },
    {
        "a":"3",
        "b":"3",
        "r":"6",
        "true": False
    },
    {
        "a":"-5",
        "b":"0",
        "r":"10",
        "true": False
    },
    {
        "a":"5",
        "b":"0",
        "r":"0",
        "true": True
    }]

    for d in data:
        if d["true"]:
            assert calc.mult(d["a"], d["b"]) == int(d["r"])
        else:
            assert calc.mult(d["a"], d["b"]) != int(d["r"])

"""bag27:2/20/2023
Holds test data in a dict. a=first operand, b=second operand, r=output, "true" determines 
if division test is supposed to be correct or incorrect. Dict is traversed and depending on "true",
division test is asserted to be equal to r or not equal."""
def test_div():
    calc = MyCalc()

    data = [{
        "a":"5",
        "b":"5",
        "r":"1",
        "true": True
    },
    {
        "a":"-25",
        "b":"5",
        "r":"-5",
        "true": True
    },
    {
        "a":"3",
        "b":"0",
        "r": "1",
        "true": False
    },
    {
        "a":"-5",
        "b":"0",
        "r":"0",
        "true": True
    },
    {
        "a":"0",
        "b":"-5",
        "r":"0",
        "true": True
    }]

    for d in data:
        if d["true"]:
            assert calc.div(d["a"], d["b"]) == int(d["r"])
        else:
            assert calc.div(d["a"], d["b"]) != int(d["r"])

"""bag27:2/20/2023
Holds test data in a dict. a=first operand, b=second operand, c= third operand, r=output, "true" 
determines if test is supposed to be correct or incorrect. Dict is traversed and first a and b are added.
the result of the addition is stored in calc.ans and used as an operand along with c as a second operation.
Depending on "true", test is asserted to be equal to r or not equal.
"""
def test_ans_add():
    calc = MyCalc()

    data = [{
        "a":"5",
        "b":"5",
        "c":"5",
        "r":"15",
        "true": True
    },
    {
        "a":"2",
        "b":"5",
        "c":"12",
        "r":"19",
        "true": True
    },
    {
        "a":"5",
        "b":"13",
        "c":"-3",
        "r":"0",
        "true": False
    }]

    for d in data:
        calc.add(d["a"], d["b"])
        if d["true"]:
            assert calc.add(calc.ans, d["c"]) == int(d["r"])
        else:
            assert calc.add(calc.ans, d["c"]) != int(d["r"])

"""bag27:2/20/2023
Holds test data in a dict. a=first operand, b=second operand, c= third operand, r=output, "true" 
determines if test is supposed to be correct or incorrect. Dict is traversed and first a and b are subtracted.
the result of the subtraction is stored in calc.ans and used as an operand along with c as a second operation.
Depending on "true", test is asserted to be equal to r or not equal.
"""
def test_ans_sub():
    calc = MyCalc()

    data = [{
        "a":"25",
        "b":"5",
        "c":"5",
        "r":"15",
        "true": True
    },
    {
        "a":"-2",
        "b":"5",
        "c":"12",
        "r":"-19",
        "true": True
    },
    {
        "a":"5",
        "b":"13",
        "c":"-3",
        "r":"0",
        "true": False
    }]

    for d in data:
        calc.sub(d["a"], d["b"])
        if d["true"]:
            assert calc.sub(calc.ans, d["c"]) == int(d["r"])
        else:
            assert calc.sub(calc.ans, d["c"]) != int(d["r"])

"""bag27:2/20/2023
Holds test data in a dict. a=first operand, b=second operand, c= third operand, r=output, "true" 
determines if test is supposed to be correct or incorrect. Dict is traversed and first a and b are multiplied.
the result of the multiplicaction is stored in calc.ans and used as an operand along with c as a second operation.
Depending on "true", test is asserted to be equal to r or not equal.
"""
def test_ans_mult():
    calc = MyCalc()

    data = [{
        "a":"5",
        "b":"5",
        "c":"5",
        "r":"125",
        "true": True
    },
    {
        "a":"2",
        "b":"-5",
        "c":"0",
        "r":"0",
        "true": True
    },
    {
        "a":"5",
        "b":"13",
        "c":"-3",
        "r":"0",
        "true": False
    }]

    for d in data:
        calc.mult(d["a"], d["b"])
        if d["true"]:
            assert calc.mult(calc.ans, d["c"]) == int(d["r"])
        else:
            assert calc.mult(calc.ans, d["c"]) != int(d["r"])

"""bag27:2/20/2023
Holds test data in a dict. a=first operand, b=second operand, c= third operand, r=output, "true" 
determines if test is supposed to be correct or incorrect. Dict is traversed and first a and b are divided.
the result of the division is stored in calc.ans and used as an operand along with c as a second operation.
Depending on "true", test is asserted to be equal to r or not equal.
"""
def test_ans_div():
    calc = MyCalc()

    data = [{
        "a":"125",
        "b":"5",
        "c":"5",
        "r":"5",
        "true": True
    },
    {
        "a":"-32",
        "b":"4",
        "c":"2",
        "r":"-4",
        "true": True
    },
    {
        "a":"30",
        "b":"10",
        "c":"0",
        "r":"0",
        "true": True
    },
    {
        "a":"25",
        "b":"5",
        "c":"2",
        "r":"4",
        "true": False
    }]

    for d in data:
        calc.div(d["a"], d["b"])
        if d["true"]:
            assert calc.div(calc.ans, d["c"]) == int(d["r"])
        else:
            assert calc.div(calc.ans, d["c"]) != int(d["r"])