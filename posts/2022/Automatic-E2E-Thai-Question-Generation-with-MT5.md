---
date: "11-8-22"
title: "Automatic E2E Thai Question Generation with MT5"
builder: "ปรินทพัฒน์ เพ็งพันธุ์ (ปริน)"
builder_info: ""
thumbnail: "/images/2022/62/01.jpg"
links:
    github: "https://parinzee.github.io/ThaiQuestionGenerationMT5/"
    facebook: "https://facebook.com/aibuildersx/posts/450060740495704"
    blog: "https://medium.com/@parinzee/studying-let-an-ai-generate-q-as-to-quiz-you-9ef27b1554d"
---

![image](/images/2022/62/01.jpg)

- โมเดลสร้างคำถาม factoid จากบทความ; แรงบันดาลใจจาการเทคนิคการทบทวนบทเรียนส่วนตัวที่จะเน้นอ่านไวๆแล้วตอบคำถามท้ายบท ปัญหาคือบางคาบเรียน เช่น วิชาประวัติศาสตร์ ไม่มีคำถามท้ายบทให้ จึงทำโมเดลเพื่อสร้างคำถามขึ้นมาเองจากเนื้อหา,
- สร้างโมเดล seq2seq ที่ทำงานประมาณนี้:, Input text: สร้าง 2 คำถาม: เฟซบุ๊ก (อังกฤษ: Facebook) เป็นบริการเครือข่ายสังคมสัญชาติอเมริกัน สำนักงานใหญ่อยู่ที่ เมนโลพาร์ก รัฐแคลิฟอร์เนีย เฟซบุ๊กก่อตั้งเมื่อวันพุธที่ 4 กุมภาพันธ์ ค.ศ. 2004, Output text: 1. เฟซบุ๊กคืออะไร A: บริการเครือข่ายสังคมสัญชาติอเมริกัน 2. เฟซบุ๊กก่อตั้งเมื่อไร A: วันที่ 4 กุมภาพันธ์ ค.ศ. 2004,
- ใช้ชุดข้อมูล question answering (เอามากลับหัวกลับหางเป็น question generation) ได้แก่ XQuAD, Thai QA (SQuAD version), iapp-wiki-qa-dataset,
- ทำความสะอาดข้อมูล เช่น HTML markup, ช่องว่างเกิน 1 ช่อง, วงเล็บที่ว่างเปล่า (ส่วนใหญ่เกิดกับบทความ Wikipedia); พบว่าหนึ่งบทความ (context) จะมีคำถามโดยทั่วไป 1-5 คำถาม,
- เลือกใช้ mT5 ผ่าน Shivanandroy/simpleT5 เพื่อปรับจูนกับชุดข้อมูลที่มี; ใส่ seperator tokens (<SEP> และ <ตัวเลข>) ระหว่างคำถามเพื่อไม่ให้โมเดลงงกับการสร้างคำถามหลายข้อ โดยเฉพาะการที่โมเดลสับสนเลขบอกข้อคำถาม (1. xxx 2. xxx) กับเลขทศนิยม (1.2 ล้านคน),
- ทำ data augmentation โดยการแตกคำถามสำหรับบทความเดียวกันเป็นหลายตัวอย่าง เช่น บทความที่มี 10 คำถาม แทนที่จะเป็นหนึ่งตัวอย่าง แตกให้เป็น 2 ตัวอย่าง ตัวอย่างละ 5 คำถาม เป็นต้น; ทำให้ได้จำนวนคำถามเพิ่มจาก 4,500 ข้อเป็น 14,000 ข้อ,
- วัดผลด้วยเกณฑ์อ้างอิงจากโครงงานคล้ายกัน patil-suraj/question_generation คือ METEOR, GLEU, BLEU-4, Chr-F, และ ROUGE-L; พบว่าโมเดลที่ใช้ data augmentation ทำคะแนนได้ดีที่สุด แต่มีปัญหาว่าไม่สามารถสร้างคำถามได้ตามจำนวนที่ต้องการนัก,
- ตรวจว่าคำถาม-ตอบ 449 คู่ที่ถูกสร้างขึ้นมาสำหรับ validation set นั้นถูกต้องแค่นั้น **ด้วยมือ** พบว่าถูกประมาณ 70%; คู่คำถาม-ตอบที่ผิดแบ่งได้เป็น อ่านไม่รู้เรื่อง (37.7%), ไม่มีคำตอบ (15.2%), จำนวนคำถามไม่ตรงตามที่ต้องการ (8.7%), คำตอบผิด (13.8%), สร้างคำถามซ้ำ ( 24.6%)

### แรงจูงในในการเข้าร่วมโครงการ (จากใบสมัครเข้าร่วมเมื่อ 10 สัปดาห์ที่แล้ว)

> "I firmly stand by the fact that I have a passion for always seeking to learn and research new things and technologies to improve myself and the world around me.  "One example of this was when I took the Harvard University CS50x course last year in grade 8. This programming course was extremely challenging. But with my passion and determination, I pressed on, excelled, and earned my certificate shown in the attached portfolio. Furthermore, I went on to completely self-study the AP Computer Science Principles course and was the only person who ever scored a perfect 5 out of 5 for my school. Currently, Im studying another Harvard course that focuses on artificial intelligence: CS50AI.",  Another achievement was the application that I wrote for my school, which is being used by over 200 people. For context, I am the youngest Student Council member in the history of my school, and I wanted to help the community by combining all the news into one place. Please see the portfolio for links to the app. During this time, I also joined the AWS Builders program to learn about the platform and all the marvelous tools that it offers.  Additionally, I am also very familiar with Linux. Throughout the last 3 to 4 years, I have researched on my own about it and have learned enough about it to post an install guide on Youtube and help countless people. To make the installation straightforward, I created various packages to add support for the Microsoft Surface devices (https://github.com/parinzee/linux-surface-overlay).  Finally, I believe that I am a compelling candidate because of my experience, ability to self-study, and extreme perseverance. These are qualities that innovators and leaders need to have. Accepting me into this program would allow me to help Thailand effectively in the future."