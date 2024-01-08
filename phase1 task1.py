class payment:
    room_no=20
    locstion='chennai'
    total=0
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.amount=0
    @classmethod
    def total_amount(cls,split):
        cls.total=split

    def split_expence(self):

        if self.total>0:
            self.amount=self.total/5
        else:
            print('invalid')
            return
        #self.amount=split

    def info(self):
        print(f'\nNAME:{self.name}')
        print(f'PHONE NUMBER:{self.phone}')
        print(f'SPLIT EXPENCE:{self.amount}\n')

    @classmethod
    def call(cls):
        while True:
            split=int(input('enter a split amount :'))
            payment.total_amount(split)

            mate1=payment('ram',0000000000)
            mate2=payment('balu',1111111111)
            mate3=payment('somu',2222222222)
            mate4=payment('suresh',3333333333)
            mate5=payment('ramesh',444444444)


            mate1.split_expence()
            mate2.split_expence()
            mate3.split_expence()
            mate4.split_expence()
            mate5.split_expence()


            mate1.info()
            mate2.info()
            mate3.info()
            mate4.info()
            mate5.info()

            print('if you want to continue-press n')
            choice=input('if you want to exist -press y :')
            
            if choice.upper() == 'Y':
                break






payment.call()





