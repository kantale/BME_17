import argparse

def amazing_function(x):
    return x*2

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Amazing program")
    parser.add_argument('value', help="Number of desired iterations")    #  Mandatory parameter
    parser.add_argument('--par', help="Value of the converge cutoff")    #  Optional parameter
    
    args = parser.parse_args()
    
    value = int(args.value)
    par = args.par
    
    print (amazing_function(value))
    if not par is None:
        print ('The value of par={}'.format(par))
        
