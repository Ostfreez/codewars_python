a = ['1,234.34', '1.324,2', '14']      
b = ['4.44', '8', '14,56']             
c = ['4.4', '8.234,1', '14,56']       
d = ['424', '8.234,1', '14,56']       
e = ['68,872', '93.854,72']           


def sum_up_numbers(numbers):
    ergebnis = 0.0
    for i in numbers:
        if len(i) <=3:
            if "," in i: i = i.replace(",", ".")
            
        else:
            if "," in i[:-3]:
                i=i.replace(",","")
            elif "." in i[:-3]:
                i = i.replace(".", "")
        if "," in i[-3:]:
            i=i.replace(",", ".")
             
        ergebnis += float(i)
    return "{:,.2f}".format(ergebnis) 
print(sum_up_numbers(a)) 
print(sum_up_numbers(b)) 
print(sum_up_numbers(c)) 
print(sum_up_numbers(d)) 
print(sum_up_numbers(e)) 