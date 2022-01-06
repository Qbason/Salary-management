from Model.Model import Model
from ViewModel.ViewLoggingModel import ViewLoggingModel
from ViewModel.ViewSignUpModel import ViewSignUpModel
from ViewModel.ViewTabsModel import ViewTabsModel

class MainViewModel():
    def __init__(self):
        self.model = Model()
        self.viewloggingmodel = ViewLoggingModel(self.model)
        self.viewsignupmodel  = ViewSignUpModel(self.model)
        self.viewtabsmodel = ViewTabsModel(self.model)