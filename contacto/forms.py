from django import forms

class FormularioPedido(forms.Form):
    Nombre = forms.CharField(label="Nombre del cliente", max_length=100, required=True)
    Email = forms.EmailField(label="Email del cliente", required=True)
    Telefono = forms.CharField(label="Teléfono del cliente", max_length=15, required=True)
    Asunto = forms.CharField(label="Asunto del cliente", max_length=100, required=True)
    Mensaje = forms.CharField(label="Mensaje del cliente", widget=forms.Textarea, required=True)

    Motivo_contacto = forms.ChoiceField(
        label="Motivo del contacto",
        choices=[
            ('soporte', 'Soporte técnico'),
            ('informacion', 'Solicitud de información'),
            ('feedback', 'Feedback'),
            ('problema_proyecto', 'Problema con un proyecto')
        ],
        required=True
    )

    Archivos_adjuntos = forms.FileField(
        label="Adjuntar archivo",  
        required=False
    )

    Preferencia_contacto = forms.ChoiceField(
        label="Preferencia de contacto",
        choices=[
            ('email', 'Correo electrónico'),
            ('telefono', 'Teléfono')
        ],
        required=False
    )

    Consentimiento_datos = forms.BooleanField(
        label="Acepto los términos y condiciones de privacidad y tratamiento de datos:",        
        required=True
    )