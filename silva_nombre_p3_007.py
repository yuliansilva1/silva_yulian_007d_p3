import funciones_validaciones as fn

while True:
    fn.mostrar_menu()
    opcion = fn.validar_opcion()
    if opcion==1:
        rut = fn.validar_rut()
        nombre_d = fn.validacion_nombre_d()
        nombre_m = fn.validacion_nombre_m()
        dias = fn.validacion_dias()
        fn.ver_habitacion()
    elif opcion==2:
         pass
    elif opcion==3:
        retirase = fn.pagar()
    else:
        despedida = fn.mensaje_despedida()
