from django.db import models
# from django.db.models.fields import CharField, DateTimeField

class Questions(models.Model):
    question = models.CharField(max_length=30)
    pub_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.question


class Choice(models.Model):
    choice = models.CharField(max_length=500)
    #here we are inheriting Questions class in choice 
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    #this is basically a counter variable
    vote = models.IntegerField(default=0)

    def __str__(self) -> str:
        #hence we are able to acess question 
        return f"{self.question} | {self.choice}"