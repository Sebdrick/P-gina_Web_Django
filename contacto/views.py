from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import FormularioPedido

def contacto(request):
    if request.method == "POST":
        formulario_pedido = FormularioPedido(request.POST, request.FILES)
        if formulario_pedido.is_valid():

            campo1 = formulario_pedido.cleaned_data.get("Nombre")
            campo2 = formulario_pedido.cleaned_data.get("Email")
            campo3 = formulario_pedido.cleaned_data.get("Telefono")
            campo4 = formulario_pedido.cleaned_data.get("Asunto")
            campo5 = formulario_pedido.cleaned_data.get("Mensaje")
            campo6 = formulario_pedido.cleaned_data.get("Motivo_contacto")
            campo7 = formulario_pedido.cleaned_data.get("Archivos_adjuntos")
            campo8 = formulario_pedido.cleaned_data.get("Preferencia_contacto")
            campo9 = formulario_pedido.cleaned_data.get("Consentimiento_datos")

            mensaje = f"""
            
            Nuevo mensaje de contacto recibido:
            
            Nombre: {campo1}
            Email: {campo2}
            Teléfono: {campo3}
            Asunto: {campo4}
            Mensaje: {campo5}
            Motivo de Contacto: {campo6}
            Preferencia de Contacto: {campo8}
            Consentimiento de Datos: {'Sí' if campo9 else 'No'}
            
            """

            email = EmailMessage(
                "Nuevo pedido recibido",
                mensaje,
                "",
                ["mac.sebas.acatlan@gmail.com"],
                reply_to=[campo2]
            )

            if request.FILES.get('Archivos_adjuntos'):
                archivos_adjuntos = request.FILES.getlist('Archivos_adjuntos')
                for archivo in archivos_adjuntos:
                    email.attach(archivo.name, archivo.read(), archivo.content_type)

            try:
                email.send()
                return redirect("/contacto/?valido")
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
                return redirect("/contacto/?novalido")
        else:
            print(formulario_pedido.errors)  
            return redirect("/contacto/?novalido")
    else:
        formulario_pedido = FormularioPedido()  

    return render(request, "contacto/contacto.html", {'miFormulario': formulario_pedido})