# 클래스

# 학생 3명의 정보를 다룬다면?
# 학생 : 이름, 학번, 학년, 성별, 점수1, 점수2


# 학생 리스트 생성
student_names_list = ["Kim", "Park", "Cho"]
student_numbers_list = [1, 2, 3]
student_grade_list = [1, 2, 3]
student_detail_list = [
    {"gender": "male", "score1": 95, "score2": 88},
    {"gender": "female", "score1": 75, "score2": 68},
    {"gender": "male", "score1": 99, "score2": 89},
]

for i in range(len(student_names_list)):
    print(
        "이름 : {}, 학번 : {}, 학년 : {}, 상세정보 : {}".format(
            student_names_list[i],
            student_numbers_list[i],
            student_grade_list[i],
            student_detail_list[i],
        )
    )
