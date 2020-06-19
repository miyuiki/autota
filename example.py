from autota.grader import Grader
from autota.recommender import Recommender

r = Recommender(pdf_path='./test.pdf', num_page=2, api_port=5555, api_url='140.115.53.158')
print(r.guiding_from(ta_ans='物件的內容透過等號來做指派'))