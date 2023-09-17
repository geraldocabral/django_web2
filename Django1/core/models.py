from django.db import models


#import submodels


# Import serico de emprestim ode chave
from .submodels.chaveModels import Chave
from .submodels.servidorModels import Servidor
from .submodels.emprestimoModels import Emprestimo