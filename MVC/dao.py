from model import *

# Classe para salvar e ler arquivo de categoria
class DaoCategoria:

    # Função para salvar arquivo de categoria
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
    
    # Função para ler arquivo de categoria
    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        # Removendo \n
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria)) 
        
        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat

# Classe para salvar e ler arquivo de venda
class DaoVenda:
    @classmethod
    def salvar(cls, venda:Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendidos.nome + '|' + venda.itensVendidos.preço + '|' +
                           venda.itensVendidos.categoria + '|' + venda.vendedor + '|' + venda.comprador + '|' +
                           str(venda.quantidadeVendida) + '|' + venda.data)
            arq.writelines('\n')


    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], i[1], i[2]),i[3], i[4], i[5]))
        return vend
    
# Classe para salvar e ler arquivo de estoque
class DaoEstoque:
    @classmethod
    def salvar(cls, produto:Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + '|' + produto.preço + '|' + 
                           produto.categoria + '|' + str(quantidade))
            arq.writelines('\n')

    
    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()


        cls.estoque = list(map(lambda x: x.replace('\n', ''),cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))
        return est
        
# Classe para salvar e ler arquivo de fornecedor
class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor:Fornecedor):
        with open('fornecedor.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + '|' + fornecedor.cnpj + '|' +
                           fornecedor.telefone + '|' + fornecedor.categoria)
            arq.writelines('\n')

        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))

        forn = []
        for i in cls.fornecedor:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
        return forn
    
# Classe para salvar e ler arquivo de pessoa/cliente
class DaoPessoa:
    @classmethod
    def salvar(cls, pessoas:Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(pessoas.nome + '|' + pessoas.telefone + '|' + pessoas.cpf + 
                           '|' + pessoas.email + '|' + pessoas.endereço)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            cls.clientes = arq.readlines()
        
        cls.clentes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

        clientes = []
        for i in clientes:
            clientes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return clientes
    
# Classe para salvar e ler arquivo de funcionários
class DaoFuncionário:
    @classmethod
    def salvar(cls, funcionário:Funcionário):
        with open('funcionários.txt', 'a') as arq:
            arq.writelines(funcionário.clt + '|' + funcionário.nome + '|' + 
                           funcionário.cpf + '|' + funcionário.email + '|' +
                           '|' + funcionário.endereço)
            arq.writelines('\n')

    
    @classmethod
    def ler(cls):
        with open('funcionários.txt', 'r') as arq:
            cls.funcionários = arq.readlines()

        cls.funcionários = list(map(lambda x: x.replace('\n', ''), cls.funcionários))
        cls.funcionários = list(map(lambda x: x.split('|'), cls.funcionários))

        funcionários = []
        for i in funcionários:
            funcionários.append(Funcionário(i[0], i[1], i[2], i[3], i[4], i[5]))
        return funcionários

