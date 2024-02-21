# Lab 1. Part 1

## Author
[Roman Kyslyi](https://www.linkedin.com/in/romankyslyi/)

## Description
On the website https://lb.ua/politics you can find many political articles.  

These articles have a publication date.  

You need to find all ***political*** articles that were written on ***February 16, 2024***. (16.02.24)  

From each article, you need to take the following information and group it as a list in the JSON format:  
 - The name of the article from the news page. (`article` field)
 - Link to the article page itself. (`link` field)
 - Article header text. (`header` field)
 - Text of the article. (`text` field)
 - Array with NER entities that are created based on the header text (`header_ner` field)
 - Array with NER entities that are created based on the text of the article (`text_ner` field)

## Example
There is an article page (see `lab1_part1_article.png` file)  

It can be converted to the following JSON output:  

``` json
[
	{
		"article": "Сенат Канади наблизив ратифікацію Угоди про вільну торгівлю з Україною",
		"link": "https://lb.ua/news/2024/02/16/598738_senat_kanadi_nabliziv_ratifikatsiyu.html",
		"header": "Сенат Канади наблизив ратифікацію Угоди про вільну торгівлю з Україною",
		"text": "Поки один парламент г альмує ухвалення позитивних для України рішень , інший рухається у цьому напрямку : Сенат Канади у другому читанні схвалив Угоду про вільну торгівлю з нашою країною . За повідомленням Укрінформу , для остаточного набуття чинності документу залишилося подолати три кроки : його має розглянути профільний комітет , після чого Сенат проведе фінальне голосування і передасть угоду на підпис генерал-губернатору – офіційному представнику короля Чарльза ІІІ , який є головою Канади . Угода про вільну торгівлю між Україною та Канадою у першій редакції діяла з 2017 року і скасовувала мита на чималу кількість товарів . У вересні 2023 Президент України Володимир Зеленський і прем'єр-міністр Канад Джастін Трюдо підписали оновлену версію документа , яка розширювала дію угоди на послуги , інвестиції , комунікації та інші перспективні галузі . Вона набуде чинності після ратифікації . Палата громад канадського парламенту свою частину процесу ратифікації Угоди про вільну торгівлю закінчила 7 лютого . Канада виділить Україні 60 мільйонів доларів для підтримки літаків F-16 . ",
		"header_ner": [
			["Канади", "LOC"],
			["Угоди про вільну торгівлю", "MISC"],
			["Україною", "LOC"]
		],
		"text_ner": [
			["України", "LOC"],
			["Сенат Канади", "ORG"],
			["Угоду про вільну торгівлю", "MISC"],
			["Укрінформу", "ORG"],
			["Сенат", "ORG"],
			["Чарльза ІІІ", "PERS"],
			["Канади", "LOC"],
			["Угода про вільну торгівлю", "MISC"],
			["Україною", "LOC"],
			["Канадою", "LOC"],
			["Президент України", "ORG"],
			["Володимир Зеленський", "PERS"],
			["Канад Джастін Трюдо", "PERS"],
			["Палата громад канадського парламенту", "ORG"],
			["Угоди про вільну торгівлю", "MISC"],
			["Канада", "LOC"],
			["Україні", "LOC"],
			["F-16", "ORG"]
		]
	},
]
```
