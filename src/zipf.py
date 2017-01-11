'''
Created on Jan 7, 2017

@author: jamey
'''

def Zipf(N, k, s=1.0):
    # f(k; s, N) = (1/k^s)/ SUM(n=1 to N, 1/n^s)
    # N = number of items in population
    # k = rank
    # s = Zipf coefficient.  > 1 is more left-skewed
    s = float(s)
    numerator = 1/pow(k,s)
    
    denominator=0
    for i in range(1, N+1):
        denominator += (1/pow(i,s))
    
    return(numerator / denominator)

def ZipfNorm(N, k, s=1.0):
    return Zipf(N, k, s)*N

'''
def main():
    N = 1500
    s = 0.5
    
    for i in range(1, 1500):
        print(i, '\tout of\t', N, '\t', '{0:.3f}'.format(Zipf(N, i, s)), '\t', '{0:.3f}'.format(ZipfNorm(N, i, s)))
        
if __name__ == '__main__':
    main()
'''