from django import forms

class AjouterCamionneurForm(forms.Form):
    
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
    photo = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    background = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'rounded py-3 px-4 block w-36 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
        })
    )
    
class UpdateCamionneurForm(forms.Form):
    
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
    

  
    