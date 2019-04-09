class assignment:
    def __init__(self, name, phone_number, sex):
        self.name = name
        self.phone_number = phone_number
        self.sex = sex

contact = []
while True:
    name = input('이름을 입력하세요 : ')
    if name == '그만':
        for i in contact:
            print('이름은' + i.name + ' 전화번호는' + i.phone_number + ' 성별은' + i.sex)
        break
    phone_number = input('전화번호를 입력하세요 : ')
    sex = input('성별을 입력하세요(male이나 female로 작성해주세요) : ')
    if sex == 'male':
        sex = 'male'
    elif sex == 'female':
        sex = 'female'
    else:
        sex = 'unknown'

    info = assignment(name, phone_number, sex)
    contact.append(info)
    for i in contact:
        print('이름은 ' + i.name + ' 전화번호는 ' + i.phone_number + ' 성별은 ' + i.sex)