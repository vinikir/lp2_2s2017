def mdc(primeiro, segundo):
    while segundo != 0:
        vezes = segundo
        segundo = primeiro % segundo
        primeiro = vezes    
    return primeiro