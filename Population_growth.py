import math


class population_growth:
    def __init__(self, in_t) -> None:
        self.N0 = 100000
        self.v = 35000
        self.t = in_t
        self.lm = 1

    def function_cal(self):
        return self.N0 * pow(math.e, self.t * self.lm) + self.v * (
                (pow(math.e, self.t * self.lm) - 1) / self.lm)

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

            self.lm = current_val
            print("lambda = " + str(self.lm) + ", output = " + str(self.function_cal()))
            calculated_vals.append(self.function_cal())
            input_vals.append(current_val)
            current_val += interval

            if current_val > end:
                setting = False
        return calculated_vals, input_vals
