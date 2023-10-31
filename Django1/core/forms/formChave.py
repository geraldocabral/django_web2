from django import forms

from ..submodels.chaveModels import Chave


# creating a form
class formChave(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = Chave

		# specify fields to be used
		fields = [
			"nome"
		]
