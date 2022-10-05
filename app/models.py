from banjo.models import Model, StringField, IntegerField

class Prediction(Model):
    statement = StringField()
    likes = IntegerField()
    dislikes = IntegerField()

    def liked(self):
        self.likes += 1

    def disliked(self):
        self.dislikes += 1

    def reset_ratings(self):
        self.likes = 0
        self.dislikes = 0
