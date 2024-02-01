# Classes Abstratas e bibliotecas ABC

Classes abstratas são como um modelo para criar outras classes  

Classe abstrata precisa ter um ou mais métodos/propriedades abstratos que devem ser implementados pelas classes filhas.  

Python tem a biblioteca ABC (Abstract Base Classes) que fornece a funcionalidade de classes abstratas.  

    A classe abstrata precisa herdar de ABC e métodos abstratos são marcados com o @decorator @abstractmethod  
    
    from abc import ABC, abstractmethod  

    Classe filha (derivada) precisa implementar todo objeto da classe abstrata.

As classes abstratas são usadas para definir a API (Application Programming Interface) de suas classes filhas.