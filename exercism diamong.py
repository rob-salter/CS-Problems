import string

def rows(letter):
    letters = string.ascii_uppercase[:string.ascii_uppercase.index(letter)+1]
    template = [' '] * (len(letters) * 2 - 1)
    middle_element = len(template)//2
    result = []

    for idx,letter in enumerate(letters):
      new_line = template.copy()
      new_line[middle_element + idx] = letter
      new_line[middle_element - idx] = letter
      result.append(''.join(new_line))
    return result + result[::-1][1:]

#print(LETTERS.index("C"))
print(rows("F"))