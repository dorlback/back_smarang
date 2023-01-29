import random as ran
import csv

def power(data):
    value = 0


    if data['age'] == '20대':
        value=value+(7*1.5)
    elif data['age'] == '30대':
        value=value+(8*1.5)
    elif data['age'] == '40대':
        value=value+(10*1.5)
    elif data['age'] == '50대':
        value=value+(9*1.5)
    elif data['age'] == '60대':
        value=value+(6*1.5)
    elif data['age'] == '70대':
        value=value+(4*1.5)


    if data['job_career'] == '1~2년':
        value=value+2
    elif data['job_career'] == '3~4년':
        value=value+4
    elif data['job_career'] == '5~6년':
        value=value+6
    elif data['job_career'] == '6~7년':
        value=value+8
    elif data['job_career'] == '8~10년':
        value=value+10
    elif data['job_career'] == '11~12년':
        value=value+12
    elif data['job_career'] == '13~14년':
        value=value+14
    elif data['job_career'] == '15~16년':
        value=value+16
    elif data['job_career'] == '17~18년':
        value=value+18
    elif data['job_career'] == '19년 이상':
        value=value+20


    if data['parti'] == '부업':
        value=value+(4*1.5)      
    elif data['parti'] == '전업':
        value=value+(8*1.5)

    if data['plat'] == 'R1':
        value=value+9
    elif data['plat'] == 'R2':
        value=value+13
    elif data['plat'] == 'R3':
        value=value+15
    elif data['plat'] == 'R4-1':
        value=value+18
    elif data['plat'] == 'R4-2':
        value=value+21
    elif data['plat'] == 'R5':
        value=value+24
    elif data['plat'] == 'R6':
        value=value+27
    elif data['plat'] == 'R7':
        value=value+30

    if data['region'] =='서울':
        value=value+14
    if data['region'] =='전체':
        value=value+20
    elif data['region'] == '경기':
         value=value+14
    else:
        value=value+6

    return(value)    


def Make_age(age):
    if age == '20대':
        return(ran.randrange(20,29))
    elif age == '30대':
        return(ran.randrange(30,39))
    elif age == '40대':
        return(ran.randrange(40,49))
    elif age == '50대':
        return(ran.randrange(50,59))
    elif age == '60대':
        return(ran.randrange(60,69))
    elif age == '70대':
        return(ran.randrange(70,90))

def Make_career(carrer):
    if carrer == '1~2년':
        return(ran.randrange(1,2))
    elif carrer == '3~4년':
        return(ran.randrange(3,4))
    elif carrer == '5~6년':
        return(ran.randrange(5,6))
    elif carrer == '7~8년':
        return(ran.randrange(7,8))
    elif carrer == '9~10년':
        return(ran.randrange(9,10))
    elif carrer == '11~12년':
        return(ran.randrange(11,12))
    elif carrer == '13~14년':
        return(ran.randrange(13,14))
    elif carrer == '15~16년':
        return(ran.randrange(15,16))
    elif carrer == '17~18년':
        return(ran.randrange(17,18))
    elif carrer == '19년 이상':
        return(ran.randrange(19,30))


def Make_plat(plat):
    if plat == 'R1':
        return(ran.randrange(1,50))
    elif plat == 'R2':
        return(ran.randrange(51,100))
    elif plat== 'R3':
        return(ran.randrange(101,500))
    elif plat == 'R4-1':
        return(ran.randrange(501,1000))
    elif plat == 'R4-2':
        return(ran.randrange(1001,5000))
    elif plat == 'R5':
        return(ran.randrange(5001,10000))
    elif plat == 'R6':
        return(ran.randrange(10001,50000))
    elif plat == 'R7':
        return(ran.randrange(50001,100000))
    
def Make_region(reg):
    if reg=='서울':
       return(14)
    if reg =='전체':
        return(20)
    elif reg == '경기':
        return(14)
    else:
        return(6)

def Make_parti(par):
    if par == '부업':
        return(4*1.5)      
    elif par == '전업':
        return(8*1.5)


f = open('write.csv','w', newline='')

wr = csv.writer(f)



age_cate = ['20대','30대','40대','50대','60대','70대']

job_cate = ['제조업','도매','서비스업','제품,개발','소프트웨어','금속','기계','건물','건설업','가공','전기','플라스틱','자동차','화물','통신','육류','운송업','의료','기타'
]

job_career_cate = ['1~2년','3~4년','5~6년','7~8년','9~10년','11~12년','13~14년','15~16년','17~18년','19년 이상']

parti_form_cate = ['부업','전업']

platform_perform_cate = ['R1','R2','R3','R4-1','R4-2','R5','R6','R7']

region_cate = ['서울','경기','인천', '강원','충북', '충남', '경북', '경남', '전북', '전남', '대전', '광주', '대구', '울산', '부산','전체']



person_list = []

# person_list.append({
#     'age' : ran.choice(age_cate),
#     'job' : ran.choice(job_cate),
#     'career' : ran.choice(job_career_cate),
#     'parti' : ran.choice(parti_form_cate),
#     'plat' : ran.choice(platform_perform_cate),
#     'region' : ran.choice(region_cate),
#     'indices' : ''
# })



for x in range(10000):
    person_list.append(
    {
    'age' : ran.choice(age_cate),
    'job_career' : [ran.choice(job_cate),ran.choice(job_cate),ran.choice(job_cate)],
    'career' : ran.choice(job_career_cate),
    'parti' : ran.choice(parti_form_cate),
    'plat' : ran.choice(platform_perform_cate),
    'region' : ran.choice(region_cate),
    'indices' : '',
    'grade':'',
    'real_age':'',
    'real_career':'',
    'real_plat':'',
    'real_region':'',
    'real_parti':'',
}
)

for x in person_list:
    x['real_age'] = Make_age(x['age'])
    x['real_career'] = Make_career(x['career'])
    x['real_plat'] = Make_plat(x['plat'])
    x['real_region'] = Make_region(x['region'])
    x['real_parti'] = Make_parti(x['parti'])
    x['indices'] = power(x)
    x['job_career'] = list(set(x['job_career']))
    
person_list = sorted(person_list, key=(lambda x: x['indices']),reverse=True)

listA = person_list[0:24900]
listB = person_list[25000:49900]
listC = person_list[50000:74900]
listD = person_list[75000:99900]

for x in listA:
    x['grade'] = 'A등급'

for x in listB:
    x['grade'] = 'B등급'

for x in listC:
    x['grade'] = 'C등급'

for x in listD:
    x['grade'] = 'D등급'

person_list = listA+listB+listC+listD

#엑셀로 출력

header_list= ['나이','지역','직업경력','경력년수','참여형식','플랫폼 실적','마케터 파워지수','등급','age','career','plat','region','parti']

wr.writerow(header_list)

for x in person_list:
    wr.writerow([x['age'],x['region'],','.join(x['job_career'] ),x['career'],x['parti'],x['plat'],x['indices'],x['grade'],x['real_age'],x['real_career'],x['real_plat'],x['real_region'],x['real_parti']])

f.close()