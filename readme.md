# AutoTA
提供BookRoll中的Marker/Memo評分功能，以及教材推薦功能
## 準備
以下四個服務需要先以docker在本地端或遠端建立
1. Question generation service(問題生成才要)
2. BERT pre-trained model service
3. BERT fine-tuned model service(簡答題評分才要)
4. Google cloud translation service(問題生成才要)

## 安裝
`pip install autota`

## 使用
獲取Marker/Memo分數
```python
from autota.grader import Grader

grader = Grader(pdf_path='./test.pdf', 
		bert_api_port=PRETRAINED_BERT_SERVICE_PORT, 
		bert_api_url='PRETRAINED_BERT_SERVICE_HOST')
print(grader.grade_marker('marker text')) #得到單一marker分數
print(grader.grade_memo('memo text')) #得到單一memo分數
```
獲取教材推薦頁數
```python
from autota.recommender import Recommender

#num_page指定要推薦多少頁
recommender = Recommender(pdf_path='./test.pdf', num_page=2, 
			api_port=PRETRAINED_BERT_SERVICE_PORT, 
			api_url='PRETRAINED_BERT_SERVICE_HOST')

print(recommender.guiding_from(ta_ans='要推薦的概念'))
#輸出為[(2, 0.0778473040773201), (1, 0.08752984923065377)]
#tuple第一項元素即為頁數，第二項為該頁與ta_ans概念間的餘弦距離
```
從教材自動生成問題
```python
from autota.generator import Generator

#num_page指定要推薦多少頁
generator = Generator(pdf_path='./test.pdf',, 
			translate_api_port=TRANSLATE_SERVICE_PORT, 
			translate_api_url='TRANSLATE_SERVICE_HOST',
			gpt2_api_port=GPT2_SERVICE_PORT,
			gpt2_api_url='GPT2_SERVICE_HOST')

print(generator.get_qa())
#輸出為[('What is the first thing that can be a variable name?', '變數名稱的第一個字不可為數字')]
#list中每個tuple為一組QA pair
```

## 開發中
1. 簡答題自動評分



