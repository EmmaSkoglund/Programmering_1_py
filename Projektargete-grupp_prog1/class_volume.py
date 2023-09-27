import math

class Volume:

    # Funktion för att beräkna volymen av en kub
    @staticmethod
    def kub_volym(sida):
        sida = float(sida)
        volym = sida ** 3
        return volym

    # Funktion för att beräkna volymen av ett rätblock (rektangelbaserat prisma)
    @staticmethod
    def rectangular_block_volym(L, B, H):
        volym = L * B * H
        return volym

    # Funktion för att beräkna volymen av ett prisma
    @staticmethod
    def prism_volym(A, H):
        return A * H

    # Funktion för att beräkna volymen av en cylinder
    @staticmethod
    def cylinder_volym(r, H):
        return math.pi * r ** 2 * H