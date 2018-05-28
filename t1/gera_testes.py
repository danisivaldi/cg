<<<<<<< HEAD
def cria_testes(n, alg):
    for i in range(1,n):
        arq = open('testes/test' + str(alg) + str(i) + '.txt', 'w')
        arq.write(str(i*100) + '\n' + str(alg) + '\n')
        arq.close()

def main():
    cria_testes(14, 1)
    cria_testes(14, 2)
    cria_testes(14, 3)

if __name__ == '__main__':
    main()
=======
<<<<<<< HEAD
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
=======
def cria_testes(n, alg):
    for i in range(1,n):
        arq = open('testes/test' + str(alg) + str(i) + '.txt', 'w')
        arq.write(str(i*100) + '\n' + str(alg) + '\n')
        arq.close()

def main():
    cria_testes(15, 1)
    cria_testes(15, 2)
    cria_testes(15, 3)

if __name__ == '__main__':
    main()
>>>>>>> 35c9c18ace90c3c70fd93a71f32504ac5969d934

# cria 15 arquivos de entrada pra cada algoritmo, variando o raio de 100 a 1500
>>>>>>> 7ca5dbc0f130fec1fa0f6d0d6695034508858d1e
