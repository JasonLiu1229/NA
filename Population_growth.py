import math


class population_growth:
    def __init__(self, in_t) -> None:
        self.N0 = 1000000
        self.v = 35000
        self.t = in_t
        self.lm = 1

    def function_cal(self, in_lm: float or int = 1):
        self.lm = in_lm
        return self.N0 * pow(math.e, self.t * self.lm) + self.v * (
                (pow(math.e, self.t * self.lm) - 1) / self.lm)

    def function_cal_newton(self, in_lm):
        self.lm = in_lm
        return self.N0 * pow(math.e, self.t * self.lm) + self.v * (
                (pow(math.e, self.t * self.lm) - 1) / self.lm) - 1264000

    def calculate(self, begin: int or float, end: int or float, left_bracket: bool = True, right_bracket: bool = True,
                  interval: float or int = 1):
        """
        Calculate every interval between the given interval
        :param begin: begin value of the interval
        :param end: end value of the interval
        :param left_bracket: if set on True, begin interval is included '['. Default on True
        :param right_bracket: if set on True, end interval is included ']'. Default on True
        :param interval: This setting will decide how big or small the intervals are
        """
        if begin >= end:
            print("Begin value can't be higher or the same as end value!")
            return
        setting = True
        current_val = begin
        calculated_vals = []
        input_vals = []
        while setting:
            if not left_bracket and current_val == begin:
                current_val += interval
                continue
            if not right_bracket and current_val >= end:
                setting = False
            # print("lambda = " + str(current_val) + ", output = " + str(self.function_cal(current_val)))
            calculated_vals.append(self.function_cal(current_val))
            input_vals.append(current_val)
            current_val += interval

            if current_val > end:
                setting = False
        return calculated_vals, input_vals

    def derivative(self, in_lm: float or int = 0):
        self.lm = in_lm
        derivative = ((self.N0 * self.t * pow(self.lm, 2) + self.t * self.v * self.lm + self.v) *
                      pow(math.e, self.lm * self.t) + self.v) / pow(self.lm, 2)
        return derivative

    def Newton(self, start_value: int or float = 0, end_value: int or float = 0, iterations: int = 1000) -> int:
        """
        Method of Newton on the population growth:
        Method of Newton = x1 = x0 - F(x0) / F'(x0)
        :param start_value: value of x0
        :param end_value: the value we want to approach
        :param iterations: How accurate we want it to be
        :return: lambda --> self.lm
        """
        cal_val = self.function_cal(start_value)
        cal_x = start_value
        out_x = cal_x
        for i in range(iterations):
            if cal_val > end_value:
                out_x = cal_x
            else:
                return out_x

            cal_x = cal_x - (self.function_cal_newton(cal_x) / self.derivative(cal_x))
            cal_val = self.function_cal(cal_x)
