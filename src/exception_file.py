import os 
import sys 

def get_error_message(error, error_details:sys):
    
    typ , er , er_tb = error_details.exc_info()
    filename = er_tb.tb_frame.f_code.co_filename

    error_message = f"Error {filename} at line_no {er_tb.tb_lineno} error message {error}"

    return error_message


class CustomException(Exception):

    def __init__(self, error , error_details:sys):
        self.error = get_error_message(error, error_details)

    def __str__(self):
        return self.error