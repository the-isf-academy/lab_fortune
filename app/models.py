from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Fortune(Model):
    fortune_statement = StringField()
    likes = IntegerField()

    category_happy = BooleanField()
    category_sad = BooleanField()

    def to_dict(self):
        return {
            'id': self.id,
            'fortune_statment': self.fortune_statement,
            'likes': self.likes,
            'category_happy': self.category_happy,
            'category_sad': self.category_sad,
        }


    def increase_likes(self):
        self.likes += 1
        self.save()


    def change_statement(self,new_statement):
        self.fortune_statement = new_statement
        self.likes = 0
        self.save()


