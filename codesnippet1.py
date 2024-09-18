input_file = open('input.txt','a')              #reads the file
output_file = open('output.txt','w')            #writes a new file called output.txt

for line_str in input_file:
  new_str =''
  line_str ='line_str.strip()                   #remove whitespaces
  for char in line_str:
    new_str = char + new_str                    #concats to the front ofa new str
print(f' line: {:12s} reverse is {:s}.format(line_str,new_str),file=output_file)'

  #Close both files
input_file.close()
output_file.close()
    
