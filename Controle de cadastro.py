class Endereco:
    def __init__(self, rua, numero, complemento, bairro, cidade, uf, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep


class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco


class Pedido:
    def __init__(self, cliente, altura, largura, frase, cor_placa, cor_letra):
        self.cliente = cliente
        self.altura = altura
        self.largura = largura
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.__valor_fixo_material = 147
        self.__valor_fixo_letra = 0.35
        self.__valor = 0
        self.numero_letras = 0
        self.area = 0
        self.custo_material = 0
        self.custo_desenho = 0

    def get_valor(self):
        a = self.frase.split()

        for i in range(0, len(a)):
            self.numero_letras += len(a[i])

        self.area = self.altura * self.largura
        self.custo_material = self.area * self.__valor_fixo_material
        self.custo_desenho = self.numero_letras * self.__valor_fixo_letra
        self.__valor = self.custo_material + self.custo_desenho
        return self.__valor

    def valor_final(self):
        valor_placa = self.__valor
        return valor_placa

    def emitir_recibo(self):
        print("Cliente:", self.cliente.nome)
        print("Telefone:", self.cliente.telefone)
        print("Largura da placa: %.1f" % self.largura)
        print("Altura da placa: %.1f" % self.altura)
        print("Frase:", self.frase)
        print("Quantidade de letras:", self.numero_letras)
        print("Valor: %.2f" % self.__valor)


class Historico:
    def __init__(self):
        self.__pedidos = []

    def inserir_pedido(self, pedido):
        self.__pedidos.append(pedido)

    def calcular_faturamento(self):
        soma = 0
        for pedidos in self.__pedidos:
            soma += pedidos.valor_final()
        return soma


def separador():
    separador = '-=' * 30
    print(separador)


'''
Instanciando Objetos:
'''

separador()
end1 = Endereco("Avenida Um", 10, '', 'Jardins', 'São Paulo', 'SP', "12345")
cli1 = Cliente("Paulo", "(11)99999-4565", end1)
ped = Pedido(cli1, 1, 3, "50% de Desconto", "Branca", "Azul")
ped.get_valor()
ped.emitir_recibo()
end2 = Endereco("Avenida dois", "11", '', 'Moema', 'São Paulo', 'SP', "02468")
separador()
cli2 = Cliente("Ana", "(11)98888-8888", end2)
ped2 = Pedido(cli2, 2, 4, "Cuidado cão bravo", "Branca", "Verde")
ped2.get_valor()
ped2.emitir_recibo()
separador()
hist = Historico()
hist.inserir_pedido(ped)
hist.inserir_pedido(ped2)
hist.calcular_faturamento()
print("O faturamento total foi de: R$ %.2f" % hist.calcular_faturamento())
separador()
