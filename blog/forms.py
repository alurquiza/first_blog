
# Para hacer que un formulario funcione necesitamos varias cosas:

# - Tenemos que mostrar el formulario. Podemos hacerlo, por ejemplo, con un sencillo {{ form.as_p }}.
# - La línea anterior tiene que estar dentro de una etiqueta de formuLario HTML: <form method="POST">...</form>.
# - Necesitamos un botón Guardar. Lo hacemos con un botón HTML: <button type='submit'>Save</button>.
# - Finalmente justo después de abrir la etiqueta <form ...> tenemos que añadir {% csrf_token %}. 
# ¡Esto es muy importante ya que hace que tus formularios sean seguros! 
# Si olvidas este pedazo, Django se molestará cuando intentes guardar el formulario:


from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
