from banjo.models import Model, StringField, IntegerField, BooleanField

class Fortune(Model):
    fortune_statement = StringField()
    likes = IntegerField()
    dislikes = IntegerField()

    category_school = BooleanField()
    category_general = BooleanField()


    def increase_likes(self):
        self.likes += 1
        self.save()

    def increase_dislikes(self):
        self.dislikes += 1
        self.save()

    def change_statement(self,new_statement):
        self.fortune_statement = new_statement
        self.likes = 0
        self.dislikes = 0
        self.save()


