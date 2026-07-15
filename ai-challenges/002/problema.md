Reto 2: El validador de contraseñas (Intermedio-Alto)

Objetivo: Manipular caracteres individuales dentro de un bucle y usar variables "bandera" (booleanas).

Escribe una función validar_password(password) que verifique si una contraseña es segura. Debe devolver True si cumple con todas las siguientes condiciones, o False si falla en alguna:

    Tener al menos 8 caracteres de largo.

    Contener al menos una letra mayúscula.

    Contener al menos un número.

    Entrada: "Arch12" -> Salida: False (muy corta)

    Entrada: "archlinux12" -> Salida: False (sin mayúsculas)

    Entrada: "ArchLinux" -> Salida: False (sin números)

    Entrada: "ArchLinux12" -> Salida: True (¡cumple todo!)