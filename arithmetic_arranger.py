import re

def arithmetic_arranger(problems, result = False):

  # Pattern #### + ####
  operation_pattern = "(^\d{1,4}) ([\+\-]) (\d{1,4}$)"
  operation_prog = re.compile(operation_pattern)

  #*********Format checker*********************

  if len(problems) > 5:
    return "Error: Too many problems."
  
  for problem in problems:
    #restarting the list
    elements = list()
    #spliting the string
    elements = problem.split() 

    #checking conditions:
    if len(elements) != 3:
      return 'Invalid format, the correct format should be: "#### + ####"'

    if re.match('(^[\*\/]$)', elements[1]):
      return "Error: Operator must be '+' or '-'."
    
    if not re.match('(^[\+\-]$)', elements[1]):
      return "Error: Operator must be '+' or '-'."

    if not re.match('^\d*$', elements[0]):
      return "Error: Numbers must only contain digits."

    if not re.match('^\d*$', elements[2]):
      return "Error: Numbers must only contain digits."

    if not re.match('^\d{1,4}$', elements[0]):
      return "Error: Numbers cannot be more than four digits."

    if not re.match('^\d{1,4}$', elements[2]):
      return 'Error: Numbers cannot be more than four digits.'

    if not operation_prog.match(problem):
      return 'Invalid format, the correct format should be: "#### + ####"'

  #arithmetic arranger
  first_line = [operation_prog.match(problem).group(1) for problem in problems]
  second_line = [operation_prog.match(problem).group(3) for problem in problems]
  operator_line = [operation_prog.match(problem).group(2) for problem in problems]
  widths = [len(first_term) + 2  
            if len(first_term) > len(second_term) 
            else len(second_term) + 2 
            for first_term, second_term in zip(first_line, second_line)]

  #chart_lines
  first_chart_line = ['{1:>{0}}'.format(width, first_term) for width, first_term in zip(widths, first_line)]
  first_chart_line = '    '.join(first_chart_line)
  second_chart_line = ['{2}{1:>{0}}'.format(width-1, second_term, operator) for width, second_term, operator in zip(widths, second_line, operator_line)]
  second_chart_line = '    '.join(second_chart_line)
  third_chart_line = ['-' * width for width in widths]
  third_chart_line = '    '.join(third_chart_line)
  
  arranged_problems = '\n'.join([first_chart_line, second_chart_line, third_chart_line])

  #if result = True then get all problems solutions:
  if result == True:
    results = [int(first_line[i]) + int(second_line[i]) if operator_line[i] == '+' 
             else int(first_line[i]) - int(second_line[i]) 
             for i in range(len(operator_line))]
    
    result_chart_line = ['{1:>{0}}'.format(width, solution) for width, solution in zip(widths, results)]
    result_chart_line = '    '.join(result_chart_line)
    arranged_problems = '\n'.join([first_chart_line, second_chart_line, third_chart_line, result_chart_line])
    

  return arranged_problems