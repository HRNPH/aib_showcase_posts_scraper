---
date: "21-7-22"
title: "Microplastic detection and collect statistical tebular data."
builder: "ภานุวัฒน์ วงศ์พัฒนวุฒิ (ก้อง)"
builder_info: ""
thumbnail: "/images/2022/41/01.jpg"
links:
    github: "https://github.com/kongonggong"
    facebook: "https://facebook.com/aibuildersx/posts/419222536912858"
    blog: "https://medium.com/@kongwongpattanawut_61910/microplastic-detection-and-collect-statistical-tebular-data-8d09339e79d"
---

![image](/images/2022/41/01.jpg)

- โมเดล object detection คัดแยก microplastic ในน้ำ แยกเป็น fragment, pellet, film, foam และ fiber,
- เก็บตัวอย่างมาจากแหล่งน้ำต่างๆในจังหวัดมุกดาหาร 6 แหล่ง และนำมาถ่ายในไมโครสโคป ยี่ห้อ Olympus CX23 กำลังขยายเลนส์ใกล้ตา 10x ใกล้วัตถุ 4x; เป็น training set 174 ภาพและ validation set 75 ภาพ,
- เพิ่มรูปและแก้ไข class imbalance (pellet และ fiber เยอะกว่าประเภทอื่นมาก) ด้วยการพลิกรูปบน-ล่าง,
- ใช้ YOLO v5l (latency น้อยกว่า) และ v5x (ประสิทธิภาพสูงกว่า); ได้ mAP[0.05:0.95] ประมาณ 0.54

### แรงจูงในในการเข้าร่วมโครงการ (จากใบสมัครเข้าร่วมเมื่อ 10 สัปดาห์ที่แล้ว)

> "ผมมีความมุ่งและมีความฝัน ที่จะผลิต คิดค้น นวัตกรรมใหม่เพื่อให้ตอบโจทย์ปัญหาทางสังคมใน ประเทศไทย และ ทั่วโลก เพื่อให้ผู้คนมี การเป็นอยู่ที่ดียิ่งขึ้น โดยการใช้เทคโนโลยี ร่วมกับ สาขาวิชา ต่างๆ อาชีพที่ผมใฝ่ฝันที่จะเป็น คือ วิศวะกรรมคอมพิวเตอร์ เพราะผมต้องการหาความรู้ด้าน คอมพิวเตอร์ เพื่อที่จะนำความรู้ที่มีมากขึ้นมาสร้าง นวัตกรรมใหม่ๆ ให้สังคม และสาขาที่อยากเรียน เสริม คือการบริหารธุรกิจ เพราะการเงินเป็นเรื่องสำคัญสำหรับทุกคน จึงอยากได้ความรู้ด้านการเงิน ควบคู่กับการสร้างนวัตกรรม เพื่อพัฒนา สังคม เเละ เศรฐกิจของไทยอย่างมั่นคงเเละยั่งยืน"