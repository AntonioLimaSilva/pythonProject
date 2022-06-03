import datetime


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite if self.__tem_limite_valido(limite) else 0
        self.__dataCriacao = datetime.datetime.now()

    def extrato(self):
        print("Numero da conta {} do titular {} tem um saldo de {} + limite {}"
              .format(self.__numero, self.__titular, self.__saldo, self.limite))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if self.__tem_saldo_disponivel(valor):
            self.__saldo -= valor
            print("Saldo efetuado")
        else:
            print("Saldo insufiente")

    def trafere(self, valorDoSaque, contaDestino):
        self.saca(valorDoSaque)
        contaDestino.deposita(valorDoSaque)

    # definindo um get
    @property
    def limite(self):
        return self.__limite

    # definindo um setter
    @limite.setter
    def limite(self, valor):
        if self.__tem_limite_valido(valor):
            self.__limite = valor
        else:
            self.__limite = 0

    @staticmethod
    def codigo_banco():
        return "001"

    # definindo um método privado
    def __tem_saldo_disponivel(self, valor):
        return valor < (self.__saldo + self.__limite)

    def __tem_limite_valido(self, valor):
        return valor > 0


if __name__ == "__main__":
    conta = Conta(103040, "Lima", 23.0, 150.0)
    conta2 = Conta(113342, "Silva", 33.0, 100.0)

    valorDoSaque = 100.0
    conta.trafere(valorDoSaque, conta2)

    conta.extrato()
    conta2.extrato()
