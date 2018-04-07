def cria_testes(n, alg):
    for i in range(1, n):
        arq = open('testes/teste' + str(alg) + str(i) + '.txt', 'w')
        arq.write(str(i*100) + '\n' + str(alg) + '\n')
        arq.close()

def main():
    cria_testes(15, 1)
    cria_testes(15, 2)
    cria_testes(15, 3)

if __name__ == '__main__':
    main()
