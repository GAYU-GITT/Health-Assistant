from .extensions import db

# tags = db.Table('tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
#     db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
# )

log_food=db.Table('log_food',
   db.Column('log_id', db.Integer, db.ForeignKey('log.id'), primary_key=True),
   db.Column('food_id', db.Integer, db.ForeignKey('food.id'), primary_key=True)
)

#we can this db to create models

class Food(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique= True, nullable=False)
    proteins = db.Column(db.Integer, nullable=False)
    carbs = db.Column(db.Integer, nullable=False)
    fats = db.Column(db.Integer, nullable=False)

    @property
    def calories(self):
        return self.proteins * 4 + self.carbs * 4 + self.fats * 9

#calories calculated from proteins, fats and carbs
#for every 1 protein/carbo there is 1 calories, for every 1 fat = 9 calories
#for each date we are going to have food items(as much as we can), each food item associated with as many dates 
#so many to many relationship

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    foods = db.relationship('Food', secondary=log_food,  lazy='dynamic')
    # tags = db.relationship('Tag', secondary=tags, lazy='subquery',
    #     backref=db.backref('pages', lazy=True))