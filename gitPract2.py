def generate_groups(g_ivbo, g_ikbo, g_imbo, g_inbo):
    IVBO = ['ИВБО-' + (lambda i: str(i) if i > 9 else '0' + str(i))(i) + '-21' for i in range(1, g_ivbo+1)]
    IKBO = ['ИКБО-' + (lambda i: str(i) if i > 9 else '0' + str(i))(i) + '-21' for i in range(1, g_ikbo+1)]
    IMBO = ['ИМБО-' + (lambda i: str(i) if i > 9 else '0' + str(i))(i) + '-21' for i in range(1, g_imbo+1)]
    INBO = ['ИНБО-' + (lambda i: str(i) if i > 9 else '0' + str(i))(i) + '-21' for i in range(1, g_inbo+1)]
    return (IVBO, IKBO, IMBO, INBO)

pr = generate_groups(8, 33, 2, 12)
for i in pr:
    print(i)