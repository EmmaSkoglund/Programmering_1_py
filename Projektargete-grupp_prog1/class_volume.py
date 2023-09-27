import math
class Volume:

    # Funktion för att beräkna volymen av en kub
    def kub_volym(s):
        volym = s ** 3
        return volym

    # Funktion för att beräkna volymen av ett rätblock (rektangelbaserat prisma)
    def rectangular_block_volym(L, B, H):
        volym = L * B * H
        return volym

    # Funktion för att beräkna volymen av ett prisma
    def prism_volym(A, H):
        return A * H

    # Funktion för att beräkna volymen av en cylinder
    def cylinder_volym(r, H):
        return math.pi * r ** 2 * H