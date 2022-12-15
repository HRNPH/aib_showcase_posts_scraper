---
date: "18-7-22"
title: "NLP for genre predictions on FFnet: an antithesis to utilitarianism"
builder: "zeiosis@"
builder_info: ""
thumbnail: "/images/2022/38/01.jpg"
links:
    github: "https://github.com/zeiosis/ffnet-summary-prediction"
    facebook: "https://facebook.com/aibuildersx/posts/417209980447447"
    blog: "https://medium.com/@cryingptosis/nlp-for-genre-predictions-on-ffnet-an-antithesis-to-utilitarianism-4380524ca1fc"
---

![image](/images/2022/38/01.jpg)

- โมเดลจำแนก genre ของ fan fiction จากบทคัดย่อด้วย BERT; แรงบันดาลใจคืออยากสร้างระบบแท้กอัตโนมัติให้ AO3 (ao3.org) เพราะแท้กปัจจุบันสร้างโดยผู้ใช้และคุณภาพไม่ค่อยดี,
- เลือก scrape ข้อมูลจาก FFNet (fanfiction.net) เพื่อเป็นชุดข้อมูล เนื่องจากแท้กใน FFNet นั้นคุณภาพเสมอต้นเสมอปลายกว่าและอนุญาตให้ใส่เพียง 2 แท้กต่อเรื่อง,
- เนื่องจากหนึ่ง fan fiction โดยทั่วไปแล้วมีมากกว่าหนึ่งแท้กจึงเลือกทำการวัดผลด้วย accuracy metric ที่ิคิดขึ้นเองคือ (% เรื่องที่มี 2 แท้กและทายถูกทั้ง 2 แท้ก) + 1/2 * (% เรื่องที่มี 1 แท้กและทายถูก) + 1/2 * (% เรื่องที่มี 2 แท้กแต่ทายถูกแค่ 1 แท้ก),
- เขียนสคริปท์สำหรับ scrape FFNet ขึ้นมาเองเนื่องจากไม่มี API อย่างเป็นทางการโดยเลือกเฉพาะเรื่องที่เป็นภาษาอังกฤษ, K->T-rated, เรื่องที่จบแล้ว และมาจากต้นฉบับที่มีงาน fan fiction อย่างน้อย 50k เรื่อง,
- พบว่ามีเพียง 8 genre หลักที่มีคนใช้เป็นแท้กคือ Romance, Humor, Drama, Hurt_Comfort, Adventure, Family, Angst, Friendship; แท้กมีความไม่สมดุลโดยเฉพาะ Romance ที่มีเยอะกว่าแท้กอื่นมาก,
- เทรนโมเดลเปรียบเทียบกับ pretrained หลาย iteration เช่น bart-large-mnli, distilbert-base-uncased-mnli และ distilbart-mnli-12-1; โมเดลที่ดีที่สุดได้ค่า accuracy ตามวิธีคิดด้านบนที่ 0.437 เทียบกับ baseline ที่ 0.269

### แรงจูงในในการเข้าร่วมโครงการ (จากใบสมัครเข้าร่วมเมื่อ 10 สัปดาห์ที่แล้ว)

> "Although I do not have much in the way of experience in actual coding or machine learning (my projects mostly being minuscule in scope and being limited to some facet of regex or language learning with Python serving as the consistent backdrop), I believe I do have a general background in the mathematical (though not so much the statistical) foundations of the course; I am comfortable with most of the basic knowledge required to do derivative and integral calculus, having learned and relearned them previously many times; however, I unfortunately do not believe I have covered the necessary background required for vector calculus, by extension from the requirement given for understanding of partial derivatives. I have in the past attempted to teach myself linear algebra as well, although I have retained little from that. I do believe, however, that my ability to focus and diligently persevere, while keeping an eye out for more efficient methods, as alluded to in the examples in regards to my mathematical education, will be a boon, should I be able to take part in the project.  I also, of course, believe in the spirit of open-source; the ability to open doors for those less fortunate than oneself should be a motivating factor for anyone, especially in a country so rife with inequality as ours. Ultimately, I wish to assist in addition to myself the general public, in order to better the opportunities afforded to anyone and everyone, regardless of social standing, geographical isolation, or otherwise."