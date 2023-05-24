from locale import atof

def square(x):
    return x**2

def main():
        
    input_txt = input('Type a number (any letter to escape): ')
    try:
        number = atof(input_txt)
    except:
        print('Exiting')

    number_squared = square(number)
    print(f'The square of {number:.2f} is {number_squared:.2f}')
    
if __name__ == '__main__':
   main() 