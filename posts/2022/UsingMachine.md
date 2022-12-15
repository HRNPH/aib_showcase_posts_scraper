---
date: "12-8-22"
title: "Using Machine Learning to create Auto Pitch Writer for UTAU"
builder: "จิรา กุลจิราพงษ์ (จิรา)"
builder_info: ""
thumbnail: "/images/2022/63/01.jpg"
links:
    github: "https://github.com/CCSleep/utau-pitch-ml/"
    facebook: "https://facebook.com/aibuildersx/posts/450681343766977"
    blog: "https://medium.com/@CCSleep/using-machine-learning-to-create-auto-pitch-writer-for-utau-eec2d104236a"
---

![image](/images/2022/63/01.jpg)

- โมเดลปรับแต่งพิช (Auto Pitch Writer) สำหรับโปรแกรมสร้างเพลง UTAU (คล้าย Vocaloid),
- [สำคัญมาก] ก่อนอื่นทำความเข้าใจ Tuning ใน UTAU ด้วยวิดีโอ https://youtu.be/ciJlUPlS7dU, , ตัวอย่างเพลงที่ไม่ได้ tune: https://youtu.be/ciJlUPlS7dU?t=59, ตัวอย่างเพลงที่ tune แล้ว: https://youtu.be/ciJlUPlS7dU?t=723, ,
- ปัญหาที่ต้องกาจะแก้คือการทำให้เพลงที่สร้างด้วยโปรแกรม "ฟังเป็นธรรมชาติขึ้น" เนื่องจากหากเราแค่ใส่พิชของแต่ละตัวโน้ตต่อกันไปเรื่อยๆจะทำให้ได้เพลงที่เหมือนหุ่นยนต์ร้อง จึงต้องมีการปรับพิชระหว่างตัวโน้ต (pitchbends) ซึ่งปกติทำด้วยมือคนแต่ง,
- เก็บข้อมูลจากลิสต์ไฟล์ UST (UTAU sequence text) ที่ถูกรวบรวมไว้ที่ https://docs.google.com/document/d/1yKn3jN3rLoVFSXcPUET_iYsmbUi-nThRktgIAyXc230/edit และใช้ไฟล์ที่ถูกเก็บด้วย Mediafire ทั้งหมด,
- UTAU แสดง pitchbends ด้วยตัวแปร 3 ตัวในรูปแบบ, , PBS=-66;-50 (เวลาเริ่ม;พิชเริ่ม), PBW=38,71,-3,141,50 (ค่าบนแกน Y นั่นคือแกนพิช สำหรับจุดถัดไป ในที่นี้คือ 4 จุด), PBY=-17.9,-18.6,-0.7,0,0 (ค่าความห่างจากจุดที่แล้วตามแกน X นั่นคือแกนเวลา), ,
- ก่อนอื่นปรับ PBS ด้วยกฎโดยให้เวลาเริ่มคือเริ่มจาก 20% สุดท้ายของความยาวโน้ตตัวที่แล้ว และเริ่มจากพิชของโน้ตตัวที่แล้ว,
- สำหรับ PBW และ PBY นั้น ใช้วิธีการสร้างโมเดล machine learning เพื่อทำนาย "เทรนด์การขึ้นลง" ของ PBY (ขึ้นเป็น 1 ลงเป็น 0; ตัวเลข 4 ตัว รวม 63 คลาส) เช่น [0,1,0,0], [0,1,1,1], ...,
- จากนั้นใช้ประสบการณ์การแต่งเพลง สร้างกฎเปลี่ยนคำทำนายกลับเป็น PBW และ PBY,
- สำหรับ feature ในการทำนาย ใช้ความยาวและพิชจากโน้ตทั้งสองตัวสร้างขึ้นด้วย pyUTAU,
- ใช้ baseline เป็นการสร้าง pitchbends ด้วย Portamento ใน UTAU คือแค่ลากเส้นขึ้น-ลงแบบเป็นเส้นตรง แน่นอนว่าจะได้เสียงที่ไม่เป็นธรรมชาตินัก,
- ใช้ random forest ได้ accuracy 61% บน test set เทียบกับ 27% ของ Portamento baseline จาก 63 classes,
- สังเกตว่าโมเดลทาย class 0 (ไม่มีพิช) และ 1 (พิชลง) มากกว่าปกติมาก (ทั้งสองคลาสเป็น 2/3 ของตัวอย่างทั้งหมด) จึงลองสร้างโมเดล logistic regression เพื่อดูว่าโมเดลคิดอย่างไร; พบว่าสำหรับ 0 โมเดลมองว่าถ้าโน้ตตัวหน้าเป็น rest แทบจะแน่นอนว่าต้องทายว่าไม่มีพิช สำหรับ 1 โมเดลมองว่าถ้าโน้ตตัวหน้าสั้นกว่าส่วนใหญ่จะเป็นพิชลง ซึ่งตรงกับสัญชาติญาณของนักแต่งเพลงที่เป็นมนุษย์

### แรงจูงในในการเข้าร่วมโครงการ (จากใบสมัครเข้าร่วมเมื่อ 10 สัปดาห์ที่แล้ว)

> "What inspires me to create AI is how I discovered NLP by accident while I was looking to create spoonerism for Thai words. Back then I really wonder how a library like PyThaiNLP can split syllables nearly perfectly without me having to tell the users to split on my own, and that really get me obsessed."