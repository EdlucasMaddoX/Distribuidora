from model import Categoria, Estoque, Produtos, Fornecedor, Pessoa, Funcionário, Venda
from dao import DaoCategoria, DaoVenda, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionário
from datetime import datetime


class ControllerCategoria:

    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe == True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print(f'Categoria cadastrada com sucesso')
        else:
            print(f'ERRO: a categoria que deseja cadastrar já existe')


    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <= 0:
            print(f'ERRO: a categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print(f'Categoria removida com sucesso')
            #TODO:COLOCAR SEM CATEGORIA NO ESTOQUE
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')


    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))
        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada)if(
                    x.categoria == categoriaAlterar)else(x), x))
                print(f'Categoria alterada com sucesso')
                #TODO: ALTERAR A CATEGORIA TAMBÉM NO ESTOQUE
            else:
                print(f'ERRO: a categoria para qual deseja alterar já existe')
        else:
            print(f'ERRO: a categoria que deseja alterar não existe')
        
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')


    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print(f'Categoria Vazia!')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')


class ControllerEstoque:
    
    def cadastrarProduto(self, nome, preço, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preço, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print(f'Produto cadastrado com sucesso')
            else:
                print(f'ERRO: o produto já existe em estoque')
        else:
            print(f'ERRO: Categoria não existe')


a = ControllerEstoque()
a.cadastrarProduto('Banana', '5', 'Verduras', 10)
