def arithmetic_arranger(problems,initial_bolean = False):
    if len(problems) > 5:
        return('Error: Too many problems.') ## check problems limit of 5

    import re
    first_line_values = []
    second_line_values = []
    operators = []
    result_line_values = []

    for problem in problems:
        expression = re.findall('(\S+)(\s)(\D)(\s)(\S+)',problem)  ## get values of problems
      
        first_value = expression[0][0]  ## check the first value
        try:
            int(first_value)  ## see if the value only contains digits
            if len(first_value) > 4:
                return('Error: Numbers cannot be more than four digits.')  ## see if number max 4 digits
            else:
                first_line_values.append(first_value)  ## append 
        except:
            return('Error: Numbers must only contain digits.')  ## 
      
        second_value = expression[0][4]
        try:
            int(second_value)
            if len(second_value) > 4:
                return('Error: Numbers cannot be more than four digits.')
            else:
                second_line_values.append(second_value)
        except:
            return('Error: Numbers must only contain digits.') 
 
        operator = expression[0][2]
        if operator == '-' or operator == '+':
            operators.append(operator)
            if operator == '+':
                result = int(first_value) + int(second_value)                
            elif operator == '-':
                result = int(first_value) - int(second_value)
            
            if result >= 0:
                result_line_values.append(' '+str(result))
            elif result < 0:
                result_line_values.append(str(result))
                
        else:
            return("Error: Operator must be '+' or '-'.")


            
    for i in range(len(first_line_values)):
        my_max = max(len(first_line_values[i]), len(second_line_values[i])) 
    
        if my_max > len(second_line_values[i]):
            dif = my_max - len(second_line_values[i])
            second_line_values[i] = (' '*(dif)) + second_line_values[i]
    
        if my_max > len(first_line_values[i]):
            dif = my_max - len(first_line_values[i])
            first_line_values[i] = (' '*(dif)) + first_line_values[i]
    

    my_first_line = ''  ## first line
    
    for i in range(len(first_line_values)):
        if i == 0:
            my_first_line = my_first_line + '  ' + first_line_values[i]
        elif i > 0:
            my_first_line = my_first_line + '      ' + first_line_values[i]
        else:
            continue


    my_second_line = ''  ## second line
    
    for i in range(len(second_line_values)):
        if i == 0:
            my_second_line = my_second_line + operators[i] + ' ' + second_line_values[i]
        elif i > 0:
            my_second_line = my_second_line + '    ' + operators[i] + ' ' + second_line_values[i]
        else:
            continue

    
    break_line = []  ## create the break line
  
    for i in range(len(operators)):
        if len(first_line_values[i]) > len(second_line_values[i]):
            spaces = '--' + '-'*len(first_line_values[i])
        elif len(first_line_values[i]) < len(second_line_values[i]):
            spaces = '--' + '-'*len(second_line_values[i])
        elif len(first_line_values[i]) == len(second_line_values[i]):
            spaces = '--' + '-'*len(second_line_values[i])
        break_line.append(spaces)
    

    my_third_line = ''
  
    for i in range(len(break_line)):
        if i == 0:
            my_third_line = my_third_line + break_line[i]
        elif i > 0:
            my_third_line = my_third_line + '    ' + break_line[i]
        else:
            continue
 

    my_result_line = ''  ## create the result line
    
    for i in range(len(result_line_values)):
        if len(result_line_values[i]) < len(break_line[i]):
            my_dif = len(break_line[i]) - len(result_line_values[i])
            result_line_values[i] = (' '*(my_dif)) + result_line_values[i]

        if i == 0:
            my_result_line = my_result_line + result_line_values[i]
        elif i > 0:
            my_result_line = my_result_line + '    ' + result_line_values[i]
        else:
            continue

    ## put everthing together

    if initial_bolean == False:
        arranged_problems = my_first_line +'\n'+ my_second_line +'\n'+ my_third_line

    elif initial_bolean == True:
        arranged_problems = my_first_line +'\n'+ my_second_line +'\n'+ my_third_line +'\n'+ my_result_line
  
    return(arranged_problems)