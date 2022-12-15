---
date: "16-7-22"
title: "Garbage Detection with Tensorflow Lite"
builder: "กันต์พัจน์ วิเศษสุข (กัน)"
builder_info: ""
thumbnail: "/images/2022/36/01.jpg"
links:
    github: "https://github.com/24GUNV/aibuilders/tree/main/object_detection/images"
    facebook: "https://facebook.com/aibuildersx/posts/415865783915200"
    blog: "https://medium.com/@24progun/object-detection-using-tensorflow-lite-80da8d75c03b"
---

![image](/images/2022/36/01.jpg)

- โมเดลคัดแยกประเภทขยะจากรูปภาพแบบ real-time ด้วย Tensorflow Lite; แยกลัง, แก้ว, โลหะ, กระดาษ และพลาสติก,
- เลือกใช้ Tensorflow Lite เนื่องจากต้องการ deploy ลง OrangePi; ต้องการความแม่นยำประมาณ 70-80% เพื่อให้ใช้งานได้จริง,
- ใช้ข้อมูลจาก asdasdasasdas/garbage-classification, mostafaabla/garbage-classification แล้วนำมา annotate เองเพื่อทำ object detection ได้เป็น training set (1,554 รูป), validation set (170 รูป) และ test set (170 รูป),
- ชุดข้อมูลที่ annotate เองเปิดให้ใช้เป็นสาธารณะที่ https://github.com/24GUNV/aibuilders/tree/main/object_detection/images ; แบ่งเป็นลัง (325 รูป), แก้ว (406 รูป), โลหะ (433 รูป), กระดาษ (199 รูป) และพลาสติก (191 รูป),
- เลือกใช้สถาปัตยกรรม EfficientDet-Lite0 เพื่อ latency ที่ดีที่สุด; ได้ AP 76.6% บน test set,
- สามารถทดลองใช้แบบ real-time ได้บน streamlit cloud; ใช้ OpenRelay เพื่อเชื่อม streamlit กับ webcam ของผู้ใช้

### แรงจูงในในการเข้าร่วมโครงการ (จากใบสมัครเข้าร่วมเมื่อ 10 สัปดาห์ที่แล้ว)

> "I wish to join the organization AI Builders because of my interest within the AI field. I had first been introduced to this field from a background of playing video games. I played these video games and gained an interest in what ran in the background of video games. I wanted to know how these games worked and soon began pursuing a way in which to learn how to code. I started of attempting to learn how to code in a language called LUA. It wasn\t easy nor very successful but it opened my eyes to what was possible with the lines of code that you could write. Wanting to know more about this, I soon ventured into a course known as CS50 (https://cs50.harvard.edu/x/2021/). I learned the basics about coding such as python, c, sql, html, etc. during this course. Wanting to know more, I continued learning after finishing this course. As someone recommended to me that there was a CS50Ai course (https://cs50.harvard.edu/ai/2020/) after that I continued to expand my knowledge and finished the course. At the same time I took "Take The World Forward Fellowship" (https://learnwithleaders.com/taketheworldforwardfellowship/) in order to attempt to apply my knowledge to make something that could be applicable in the real world. Now I believe that the next step for me is to join "AI Builders" in order for my next step to apply my knowledge into something in the real world.  I wish to be a part of AI Builders because I have an interest in the AI field. I believe that AI, in the future, will be a major part of our lives. I think that by joining with this organization, I build upon and learn new concepts and lessons and apply them to the projects that I can make in the real world. I think that this organization is greater than doing it individually since we can ask the mentors from the organizations and our peers for advice on for our specific project. These mentors have experience in doing this type of stuff so it would be greatly beneficial to have them guide us through this experience. Another benefit of this organization is that they have prepared us lessons which can also guide us when creating this project. We can learn new concepts in which we can immediately use them in the real world by incorporating them into the projects that we are making.  During my time at the "AI builders" program, I plan to construct garbage classification machine. It should be able to the differentiate the different types of materials. An image from a camera set up inside the machine take a picture of the garbage that the user puts in. Then, based on the image, an AI will classify the type of garbage that it is. It can classify the items by the material of the item. Lastly, there will be a mechanism in the machine that can push the garbage into its specific garbage chute. This machine will help group the same types of material together, hopefully making recycling easier since the garbage is classified into different materials."