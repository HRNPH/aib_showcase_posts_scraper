---
date: "28-7-22"
title: "TLDR; Terms and Conditions Summarizer"
builder: "ศุภโชค บุตรดีขันธ์ (บูม)"
builder_info: ""
thumbnail: "/images/2022/48/01.jpg"
links:
    github: "https://github.com/Mikune00/ai-text-sum"
    facebook: "https://facebook.com/aibuildersx/posts/427644922737286"
    blog: "https://medium.com/@kaitosolo18/terms-and-condition-summarization-d7f0680f752b"
---

![image](/images/2022/48/01.jpg)

- ผลจากการสำรวจประชากร Gen Z 100 คนชาวไทยพบว่าเพียง 92% เห็นว่าข้อกำหนดและเงื่อนไขมีความสำคัญ แต่มีเพียง 1% ที่อ่านเต็มๆทุกครั้ง เนื่องจากมันยาวมาก ข้อมูลเยอะเกินไป ไม่น่าอ่านด้วย เสียเวลา และอื่น ๆ อีกมากมาย, "
- เก็บข้อมูลจากเว็บไซต์ Terms of Service; Didnt Read ที่ประกอบด้วยข้อกำหนดและเงื่อนไขตัวเต็มและคำย่อที่เว็บไซต์ย่อมาให้แล้ว",
- ทำความสะอาดข้อมูลด้วยการลบอักษรพิเศษ ช่องว่างส่วนเกิน และข้อความที่ไม่มีคู่คำย่อ,
- ข้อความตัวเต็มส่วนใหญ่มีความยาวราว 100-200 คำและมากที่สุดถึง 1600 คำ ส่วนคำย่อมีความยาวเฉลี่ย 10 คำ,
- เทรนด้วยสถาปัตยกรรม T5; แบ่งชุดข้อมูลเป็น train-validation-test ที่ 70-20-10,
- ได้ผล ROUGE-1 F1 0.66, ROUGE-2 F1 0.52 และ ROUGE-L F1 0.61; เปรียบเทียบกับ baseline คือการทำ sentence retrieval ด้วย T5 ได้ดีกว่าประมาณ 3-5 เท่า,
- Open Source บน HuggingFace Hub

### แรงจูงในในการเข้าร่วมโครงการ (จากใบสมัครเข้าร่วมเมื่อ 10 สัปดาห์ที่แล้ว)

> "ผมได้เข้าร่วมเเข่งขันโครงงานวิทยาศาสตร์สาขาวิทยาการข้อมูลเเละได้ทำโครงงานเกี่ยวกับการใช้เขียนโปรแกรมเเจ้งเตือนอัตโนมัติผ่าน line โดยใช้ข้อมูลจากกรมอุตินิยมวิทยา4ปีย้อนหลังในการคาดคะเนการเกิดอุทุกภัย เเละโครงงานนี้เองที่เป็นเเรงบันดาลใจในการศึกษาด้านต่อในเรื่อง ai เพื่อนำไปประยุต์ใช้กับปัญหาต่างๆในอนาคตเเละผมมั่นใจว่าถ้าหากผมได้รับเข้าโครง AI Builders 2022 จะให้ความร่วมมือเเละตั้งใจอย่างถึงที่สุดครับ  มีความสนใจในเรื่อง ai เพราะในปัจจุบัน ai เป็นที่พูดถึงอย่างมากเเละในอนาคตอันใกล้นี้ ai อาจมีบทบาทมากขึ้นกว่าปัจจุบันผมจึงอยากพัฒนาฝีมือของตัวเองพร้อมทั้งหาเรื่องที่ท้าทายมากขึ้นเละเล็งเห็นว่าโครงการ AI Buildersนี้สามารถให้ความรู้กับผมเพื่อไปพัฒนาเเละต่อยอดได้เห็นได้จากผลงานของพี่ๆที่เคยเข้าร่วมโครงการนี้ ทุกผลงานมีการประยุตก์ใช้ในการแก้ปัญหาต่างๆได้อย่างเหมาะสมผมจึงอยากที่จะเข้าร่วมโครงการ AI Builders 2022 เพื่อสามารถพัฒนาเเละแก้ปัญหาต่างได้อย่างกับพี่ๆที่เคยเข้าร่วมโครงการนี้ครับ"