def arithmetic_arranger(problems, *display):
  arranged_problems = ''

  first_row = ''
  second_row = ''
  third_row = ''
  fourth_row = ''

  if(len(problems) > 5):
    return 'Error: Too many problems.'
  
  for problem in problems:
    elements = problem.split()
    problem_size = len(max(elements, key=len))+2
    result = 0

    try:
      int(elements[0])
      int(elements[2])
    except:
      return "Error: Numbers must only contain digits."
    
    if len(str(elements[0])) > 4 or len(str(elements[2])) > 4:
      return "Error: Numbers cannot be more than four digits."

    if elements[1] == '+':
      result = int(elements[0]) + int(elements[2])
    elif elements[1] == '-':
      result = int(elements[0]) - int(elements[2])
    else:
      return "Error: Operator must be '+' or '-'."

    first_row  += ' '*(problem_size - len(elements[0]))+elements[0] + ' ' * 4 
    second_row += elements[1]+' '*(problem_size - len(elements[2])-1)+elements[2] + ' ' * 4 
    third_row  += '-'*problem_size + ' ' * 4
    fourth_row += ' '*(problem_size -len(str(result)))+str(result) + ' ' * 4

  if display == (True,):
    arranged_problems = first_row[0:len(first_row)-4] + '\n' + second_row[0:len(second_row)-4] + '\n' + third_row[0:len(third_row)-4] + '\n' + fourth_row[0:len(fourth_row)-4]
  else:
    arranged_problems = first_row[0:len(first_row)-4] + '\n' + second_row[0:len(second_row)-4] + '\n' + third_row[0:len(third_row)-4]


  return arranged_problems