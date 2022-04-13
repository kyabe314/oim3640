import random
class Covid:
    #base_sequence = 'Base Sequence'
    """This is a class of Covid. Each covid should have a base sequence, and extension"""

    base_sequence = "abcd"

    def __init__(self, name='unknown_covid', new_seq='###'):
        self.name = name
        self.extension = new_seq
        self.sequence = self.base_sequence + '.' + self.extension
        # self.sequence = new_seq
        # if random.random() < 0.25:
        #     self.sequence =  self.base_sequence + new_seq
        # else:
        #     self.sequence = self.base_sequence
    
    def replicate(self):
        """return a new Covid instance by replicating itself"""
        return Covid(
            name="new"+self.name,
            new_seq=self.sequence)
    
    def __add__(self, another_covid):
        """"""
        new_seq = ''.join(random.choices(self.extension+another_covid.extension, k=3))
        return Covid(name='New Covid from Mixing', new_seq=new_seq)
    
    def __str__(self, another_covid):
        return f'{self.name}: {self.sequence}'


covid_0 = Covid() # creating an instance of Covid by invoking the initializing method, __init__
covid_1 = Covid(name='second_case',new_seq="123")

print(covid_0.sequence)
print(covid_1.sequence)
covid_2 = covid_1.replicate()
print(covid_2.sequence)
print(covid_2.mix(covid_0).sequence)
covid_3 = covid_0 + covid_2
print(covid_3)

