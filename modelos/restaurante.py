class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
     print(f'{"nome do restaurante".ljust(25)} | {"categoria".ljust(25)} | {"status".ljust(25)}')
     for restaurante in Restaurante.restaurantes:
        print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
       self._ativo = not self._ativo
