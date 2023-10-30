# radia.danae.main.py
"""Página de entrada do jogo Ilha Proibida.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    23.10
    Classes Ilha, Terreno, Peao (10).
    
.. versionadded::    23.09
    Versão Inicial (26).

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""

from _spy.vitollino.main import Cena, Elemento, STYLE

STYLE["width"] = 800
STYLE["height"] = "600px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
VALE_TENEBROSO = "https://i.imgur.com/OZE1myn.jpg"
PORTAO_OURO = "https://i.imgur.com/PvkZSQP.jpg"
PORTAO_COBRE = "https://i.imgur.com/45aU3nf.jpg"
ATALAIA = "https://i.imgur.com/sdJ4W5O.jpg"
JARDIM_SUSSUROS = "https://i.imgur.com/pjVcyoy.jpg"
PISTA_POUSO = "https://i.imgur.com/CU3TLYh.png"
JARDIM_UIVOS = "https://i.imgur.com/ZNuPWqZ.jpg"
PAWN = "https://imgur.com/zO3kiRp.png"


class IlhaProibida:
    """ Representa a classe principal do Jogo.
    
    Terrenos 
        Locais onde os peões podem ficar.
        
    """

    def __init__(self):
        self.oceano = Cena(IMAGEM).vai()
        self.terrenos = []
        self.monta_tabuleiro_oceano()
        #self.peao = Peao(self)
        #self.peao.mover(self.terrenos[0])

    def monta_tabuleiro_oceano(self):
        """ Montar o tabuleiro em forma de diamante.
        
        """
        info_terrenos = [PORTAO_OURO, PALACIO_CORAL, PORTAO_BRONZE, VALE_TENEBROSO, PORTAO_COBRE, ATALAIA, PISTA_POUSO] * 9
        self.terrenos = [Terreno(cena=self.oceano, posy=px // 6,
                                 posx=((px % 6) + int(abs(2.5 - px // 6))), local=lc, ilha=self)
                         for px, lc in enumerate(info_terrenos[:36]) if px % 6 < 6 - int(abs(2.5 - px // 6)) * 2]
        #self.terrenos[4].afundar()


class Terreno:
    """ Local onde um peão pode ficar.

    :param local: Imagem do terreno
    :param posx: Coordenada x do terreno.
    :param posy: Coordenada y do terreno.
    :param cena: Cena do local.
    :param ilha: Referência ao tabuleiro.
    """

    def __init__(self, local, posx, posy, cena, ilha):
        self.local = Elemento(local, x=posx * 110 + 10, y=posy * 110 + 50, w=100, h=100,
                              cena=cena)
        self.peao, self.ilha = None, ilha
        self.posx, self.posy = posx, posy
        #self.local.vai = self.vai
        self.afunda = False


if __name__ == "__main__":
    # IlhaProibida()
    IlhaProibida()
