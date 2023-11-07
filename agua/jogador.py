# radia.agua.jogador.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""Classes Relacionadas com o Jogador.

LOG - http://bit.ly/Dev_Agile_23

EQUIPE Água

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>
.. codeauthor:: Julia <julia@gmail.com>

Changelog
---------
.. versionadded::    23.11
    Classe Jogador e MaoJogador (07).

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""


class Jogador:
    def __init__(self):
        self.mao = MaoJogador(dono=self)
        self.nome = "Navegador"
        print(f"{self.nome} se apresentando")


class MaoJogador:
    def __init__(self, dono, cartas=[]):
        self.dono = dono
        self.cartas = cartas
        print(f"A mão do {self.dono.nome} possui {len(self.cartas)} cartas")
        
        
if __name__ == "__main__":
    #IlhaProibida()
    Jogador()
    