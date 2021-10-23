##Mapping values to change int to roman
int_rom = [(1000,'M'), (500,'D'), (100,'C'), (50,'L'), (10,'X'), (5,'V'), (1,'I')]

##Define function to convert
def integerToRoman(num):
    ##Initialize result variable
    rom = ''

    while(num > 0):
        for n,r in int_rom:
            ##Check if we can divide with map values to change
            while num >= n:
                ##Add the value to result
                rom = rom + r
                ##Calculate new value to process
                num = num - n
    return rom

print(integerToRoman(525))
