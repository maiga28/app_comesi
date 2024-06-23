from django import forms
from django.core.exceptions import ValidationError
from main_apps.comionneur.models import Camionneur

class AjouterCamionneurForm(forms.ModelForm):
    class Meta:
        model = Camionneur
        fields = [
            'username', 'nom', 'prenom', 'numero_de_telephone', 'email', 
            'entreprise_employeur', 'numero_de_permis', 'experience', 
            'type_de_camion_conduit', 'date_de_naissance', 'photo', 'background'
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'nom': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'prenom': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'numero_de_telephone': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'entreprise_employeur': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'numero_de_permis': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'experience': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'type_de_camion_conduit': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'date_de_naissance': forms.DateInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'background': forms.ClearableFileInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Camionneur.objects.filter(username=username).exists():
            raise ValidationError("Ce nom d'utilisateur existe déjà. Veuillez en choisir un autre.")
        return username

    
class UpdateCamionneurForm(forms.ModelForm):
    class Meta:
        model = Camionneur
        fields = [
            'username', 'nom', 'prenom', 'numero_de_telephone', 'email', 
            'entreprise_employeur', 'numero_de_permis', 'experience', 
            'type_de_camion_conduit', 'date_de_naissance', 'photo', 'background'
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'nom': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'prenom': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'numero_de_telephone': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'entreprise_employeur': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'numero_de_permis': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'experience': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'type_de_camion_conduit': forms.TextInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'date_de_naissance': forms.DateInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
            'background': forms.ClearableFileInput(attrs={
                'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            }),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Camionneur.objects.filter(username=username).exists():
            raise ValidationError("Ce nom d'utilisateur existe déjà. Veuillez en choisir un autre.")
        return username
    
class AjouterClientForm(forms.Form):
    
    nom = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    prenom = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': ' rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    numero_de_telephone = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'rounded py-3 px-4 block w- border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    entreprise_employeur = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    numero_de_permis = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    experience = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    type_de_camion_conduit = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    date_de_naissance = forms.CharField(
        widget=forms.DateInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    
class AjouterDemandeForm(forms.Form):
    
    nom = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    prenom = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': ' rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    numero_de_telephone = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'rounded py-3 px-4 block w- border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    entreprise_employeur = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    numero_de_permis = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    experience = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    type_de_camion_conduit = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    date_de_naissance = forms.CharField(
        widget=forms.DateInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    
class AjouterCamionForm(forms.Form):
    
    nom = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    prenom = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': ' rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    numero_de_telephone = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'rounded py-3 px-4 block w- border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    entreprise_employeur = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    numero_de_permis = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    experience = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    type_de_camion_conduit = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    date_de_naissance = forms.CharField(
        widget=forms.DateInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    

  
    