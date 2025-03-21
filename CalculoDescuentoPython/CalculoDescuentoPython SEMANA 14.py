def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a un monto total.

    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (int, opcional): El porcentaje de descuento a aplicar. Por defecto es 10.

    Retorna:
    float: El monto del descuento calculado.
    """
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Llamadas a la función
monto1 = 125.00
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

monto2 = 150.00
porcentaje_descuento2 = 20
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
monto_final2 = monto2 - descuento2

# Salida de resultados
print(f"Monto total: ${monto1}, Descuento: ${descuento1}, Monto final: ${monto_final1}")
print(f"Monto total: ${monto2}, Descuento: ${descuento2}, Monto final: ${monto_final2}")