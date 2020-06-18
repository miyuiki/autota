from autota.grader import Grader

grader = Grader(pdf_path='./test.pdf', bert_api_port=5555, bert_api_url='140.115.53.158')
print(grader.grade_marker(''))
print(grader.grade_memo('123'))