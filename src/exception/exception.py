import sys

class customexception(Exception):
    
    def __init__(self, error_msg, error_info:sys):
        self.error_msg = error_msg
        _,_,exec_tb = error_info.exc_info()
        print(exec_tb)
        self.lineno = exec_tb.tb_lineno
        self.filename = exec_tb.tb_frame.f_code.co_filename
    
    
    def __str__(self):
        return f"Error occured in file {self.filename} at line number {self.lineno}.\nError: {self.error_msg}"
    
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        raise customexception(e, sys)