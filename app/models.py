from banjo.models import Model, StringField

class Prediction(Model):
    statement = StringField()
