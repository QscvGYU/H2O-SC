# coding = 'utf-8'


class ParameterException(Exception):
    def __int__(self, error_msg):
        self.msg = error_msg

    def __str__(self):
        return f"parameter error {self.msg}"