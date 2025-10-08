from django import forms

class FormContacto(forms.Form):
    OPTIONS = (
        ("WSP", "Mensaje de texto (WhatsApp)"),
        ("EMAIL", "Correo electrónico"),
        ("CALL", "Llamada telefónica"),
    )
    nombre = forms.CharField()
    email = forms.CharField()
    nTelefono = forms.CharField()
    formaContacto = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
    mensaje = forms.CharField()

    nombre.widget.attrs['class'] = "form-control"
    email.widget.attrs['class'] = "form-control"
    nTelefono.widget.attrs['class'] = "form-control"
    mensaje.widget.attrs['class'] = "form-control"