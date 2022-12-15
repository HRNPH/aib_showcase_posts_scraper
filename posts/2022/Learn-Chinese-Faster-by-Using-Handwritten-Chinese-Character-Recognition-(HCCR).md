---
date: "30-7-22"
title: "Learn Chinese Faster by Using Handwritten Chinese Character Recognition (HCCR)"
builder: "ภควุฒิ ธรรมาวุฒิกุล (Army)"
builder_info: ""
thumbnail: "/images/2022/50/01.jpg"
links:
    github: "https://github.com/GithubArmy/Handwritten-Chinese-Character-Recognition"
    facebook: "https://facebook.com/aibuildersx/posts/429664732535305"
    blog: "https://medium.com/@army.prakawut/learn-chinese-faster-by-using-handwritten-chinese-character-recognition-hccr-67b23c63fb9"
---

![image](/images/2022/50/01.jpg)

- โมเดลทำนายตัวอักษรภาษาจีนจากลายมือ 1,059 ตัวใน HSK4 และ 7,330 ตัวที่ใช้บ่อยด้วย resnet34; ใช้ได้ทั้งทาง webapp และบน Raspberry Pi,
- ชุดข้อมูลจาก Institute of Automation of Chinese Academy of Sciences; แปลงเป็น png ในชุดข้อมูล pascalbliem/handwritten-chinese-character-hanzi-datasets บน Kaggle,
- ข้อมูลแบ่งเป็น train ประมาณ 600 รูปต่อตัวอักษรและ test ประมาณ 140 รูปต่อตัวอักษร,
- เทรนโมเดล ResNet18, ResNet34 และ MobileNetV2 ด้วย GPU บนโน้ตบุ๊คของตัวเอง,
- ได้ accuracy 97.3% บนชุดข้อมูล HSK4 (1,059 ตัวอักษร) และ 94.4% บนชุดข้อมูล 7,330 ตัวอักษร,
- ศึกษาคุณภาพของโมเดลด้วยการให้คน 15 คนลองใช้ webapp บน Huggingface ค้นพบว่าการเขียนผิด เช่น องศาของเส้น มีผลต่อความมั่นใจของโมเดล; โมเดลที่เทรนบนชุดข้อมูล 7,330 ตัวอักษรมีตัวอักษรที่ไม่ใช่อักษรจีน เช่น\u3000≠ ถูกสับสนกับ\u3000半,
- พบว่าโมเดลทำนาย 一 (เลขหนึ่ง) ได้ยากมาก (ถูกเพียงหนึ่งในสิบครั้งโดยเฉลี่ย); เหตุผลคือภาพที่ถูกเทรนเป็นสี่เหลี่ยมผืนผ้า และเมื่อถูกบีบให้เป็นสี่เหลี่ยมจตุรัสระหว่างเทรนจึงทำให้ได้ผลที่ไม่ดี; แก้ไขด้วยการปรับขนาดให้ถูกต้อง,
- โมเดลสามารถใช้ได้ทั้งผ่าน webapp, Raspberry Pi 3b+ และ Raspberry Pi Zero 2w

### แรงจูงในในการเข้าร่วมโครงการ (จากใบสมัครเข้าร่วมเมื่อ 10 สัปดาห์ที่แล้ว)

> "I have been coding since I was young, so I would understand the concept faster. I have experience in coding microcontrollers using C language and competing in several robotic competitions, but I have never made any project about AI. This is a very great opportunity for me to start learning and using AI. If I were able to make AI, I could also use it to develop other projects and skills, like applying AI into robots. I believe that understanding AI would help in my later studies and jobs as AI are becoming more desired in companies over the years. I would also give my best and as much time as needed to finish the project. I have high stamina and diligence. I would never give up solving what I had started.  I really want to join the course as I want to be able to make AI project and code Python. Nowadays, AI is founded almost everywhere, but I still don’t understand what it is and how it works. Or even how good it is that it is so widely founded and common. I think these questions will be all clear to me if I join this course. I know that everything is going into the digital world, and AI & coding skills are greatly appreciated. Therefore, knowing how to use Python and make AI would really make me accomplished more in future. Making an AI project would also be really fun as I would have to embrace harder challenges and coding bugs. I have never used Python before, so when I watched your videos about Python, NumPy, and Pandas, it was really fascinating to me. I always enjoy the feeling when I finally solve each of the questions in this Python Exam."