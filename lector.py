# Abre el archivo en modo lectura
with open('wifi.txt', 'r') as file:
    # Lee cada línea del archivo
    for line in file:
        # Divide la línea en palabras usando ',' como separador
        words = line.split(',')
        # print(words)
        # Itera sobre las palabras y busca las que contienen 'SSID' y 'pass'
        ssid = None
        password = None
        for word in words:
            if 'SSID' in word:
                # Extrae el SSID eliminando 'SSID: ' de la palabra
                ssid = word.split(':')[1]                
            elif 'PASS' in word:
                # Extrae la contraseña eliminando 'pass: ' de la palabra
                password = word.split(':')[1]

        # Imprime la información
        # print(ssid)
        if ssid and password:
            print(f"SSID: {ssid}, Contraseña: {password}")