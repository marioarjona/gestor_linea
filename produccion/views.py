
from django.http import HttpResponse
from django.utils import timezone


def inicio(request):
    ahora = timezone.localtime().strftime("%d/%m/%Y %H:%M")
    html = f"""
    <html>
    <head><meta charset="utf-8"><title>Gestor de Línea</title></head>
    <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>Gestor de Línea de Producción</h1>
        <p>Proyecto inicial en Django funcionando correctamente.</p>
        <p><b>Fecha y hora del servidor:</b> {ahora}</p>
        <h2>Módulos previstos</h2>
        <ul>
            <li>Registro de placas y equipos probados</li>
            <li>Solicitud y seguimiento de material pendiente</li>
            <li>Inventario de repuestos</li>
            <li>Organización de turnos y personal</li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html)