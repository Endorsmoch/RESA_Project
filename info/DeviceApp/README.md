# Algoritmo de recorrido de dispositivos

## Datos de entrada para la lectura

A continuación, se definen los datos mínimos que deberán enviarse a modo de diccionario al método `load_configuration`:

```JSON
{
  "id": "mac-add-1",
  "neighbours": [
    {"id": "mac-add-2", "ips": ["192.168.10.6"]},
    {"id": "mac-add-3", "ips": ["192.168.10.10"]}
  ],
  "ips": ["192.168.10.1", "172.16.1.1"]
}
```

## Proceso de lectura

1. Mandar petición de reconocimiento de vecinos a una dirección IP por defecto
2. Formatear los datos de la respuesta para que se ajusten al estándar requerido
3. Enviar los datos al método `load_configuration`
4. Llamar a `next_device` para recuperar el objeto `Device` a explorar
5. Por cada dirección IP especificada en el dispositivo, envíe la petición de reconocimiento de vecinos y repita los pasos **2** y **3**
6. Cuando ya se hayan evaluado todas las direcciones IP del dispositivo, repita los pasos **4** y **5**
7. Si la respuesta del paso **4** fue `None`, la topología ya fue escaneada en su totalidad
