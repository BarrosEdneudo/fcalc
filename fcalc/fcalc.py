def js_acum(pv, i, n):
    """
    Retorna o valor acumulado de juros simples.

    :param pv: Valor presente, capital ou principal
    :param i: Taxa de juros percentual.
    :param n: Quantidade de períodos considerados.

    """

    return pv * (i / 100) * n

def tx_juros(j, pv):
    """
    Retorna a taxa de juros percentual.

    Taxa de juros é a razão entre os juros recebidos (ou pagos) ao final de um período de tempo e o capital inicialmente empregado.

    :param j: Valor monetário dos juros recebidos (ou pagos).
    :param pv: Valor do capital ou principal.



    """

    return (j / pv) * 100

def montante_simples(pv, i, n):
    """
    Retorna o montante (capital + juros) de um capital aplicado à uma taxa de juros simples em um dado período.

    :param pv: Valor atual, capital ou valor presente.
    :param i: Taxa percentual de juros simples.
    :param n: Quantidade de períodos.
    """


    return pv * (1 + (i / 100) * n)

def montante(pv, i, n):
    """
        Retorna o montante (capital + juros) de um capital aplicado à uma taxa de juros compostos em um dado período.

        :param pv: Valor atual, capital ou valor presente.
        :param i: Taxa percentual de juros compostos.
        :param n: Quantidade de períodos.
    """

    return pv*(1 + (i/100))**n

def price(pv, i, n):
    """
    Retorna a prestação periódica de um empréstimo baseado no sistema price, também conhecido como sistema francês de amortização.

    A função não diferencia o período (quantidade de prestações), que pode estar em ano, mês ou qualquer outro. Deve-se atentar, entretanto, para o fato de que os parâmetros i e n devem estar no mesmo período.

    :param pv: Valor presente, valor atual, valor principal ou capital.
    :param i: Taxa de juros na forma percentual. exs: 1.3 , 2.0 , 0.25
    :param n: Quantidade de prestações.

    """

    return round(pv * ((((1 + (i / 100)) ** n) * (i / 100)) / (((1 + (i / 100)) ** n) - 1)), 2)

def equivalente(i, n):

    """
    Retorna a taxa percentual equivalente anual para a taxa e período passados como parâmetros, sendo n (string):
        d == dia;
        m == mês;
        b == bimestre;
        t == trimestre;
        q == quadrimestre
        s == semestre;

    :param i: Taxa atual na sua forma percentual
    :param n: Período atual
    """

    if n == 'd':
        n = 360
    elif n == 'm':
        n = 12
    elif n == 'b':
        n = 6
    elif n == 't':
        n = 4
    elif n == 'q':
        n = 3
    elif n == 's':
        n = 2
    else:
        n = i

    equivalente =  (((1+(i/100))**n)-1)*100
    
    return round(equivalente,2)