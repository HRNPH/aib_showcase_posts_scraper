---
date: "17-7-22"
title: "Sick Pig Classifier"
builder: "ภวัต ลีชาแสน (บีม)"
builder_info: ""
thumbnail: "/images/2022/37/01.jpg"
links:
    github: "https://github.com/Igonazio/Sick-Pig-Classifier"
    facebook: "https://facebook.com/aibuildersx/posts/416533550515090"
    blog: "https://medium.com/@beamsisb/sick-pig-classifier-394db89c3c5d"
---

![image](/images/2022/37/01.jpg)

- โมเดลแยกแยะรูปหมูป่วยด้วย ResNet-18; แรงบันดาลใจจากข่าวโรคอหิวาต์แอฟริกาในสุกร (African swine fever : ASF) ระบาดช่วงต้นปี 2022,
- ต้องการโมเดลที่ขนาดเล็กสามารถใช้งานได้ง่าย และมีความแม่นยำเพียงพอในการทุ่นแรงมนุษย์ โดยอาจไม่แม่นยำเท่ามนุษย์เนื่องจากการวินิฉัยโรคใช้มากกว่าการมองเห็น,
- สร้างชุดข้อมูลจากการ scrape รูปจากอินเตอร์เน็ต; พบปัญหารูปหมูป่วยหาได้ยาก และรูปหมูไม่ป่วยบางครั้งมีรูปที่ไม่เกี่ยวข้อง เช่น การ์ตูน Peppa Pig ติดมาด้วย; ได้รูปหมูป่วยทั้งหมด 141 รูป หมูไม่ป่วย 370 รูป,
- ResNet-18 ได้ผลดีที่สุดบน test set จำนวน 154 รูป ได้ micro-averaged F1 ที่ 0.84; เทียบกับ baseline การทายว่าทุกตัวไม่ป่วยที่ 0.82 (แน่นอนว่าในกรณีนี้ recall ของหมูป่วยเป็น 0) และ CNN ที่ 0.63,
- โมเดลที่ดีที่สุดมี recall (จำนวนหมูป่วยที่ทายถูก / จำนวนหมูป่วยทั้งหมด) สูงถึง 0.88 ซึ่งน่าจะเพียงพอสำหรับการช่วยคนเฝ้าระวังในฟาร์ม,
- จำเป็นต้องทดลองกับภาพจริงในฟาร์ม เพื่อพัฒนาสู่ระบบใช้งานจริง

### แรงจูงในในการเข้าร่วมโครงการ (จากใบสมัครเข้าร่วมเมื่อ 10 สัปดาห์ที่แล้ว)

> "I am a highly-motivated person who strives to make a difference in Thai society. I have a habit of observing the problems that various groups of people around me have been facing and thinking about the solutions to their problems. For instance, as flooding becomes a frequent natural disaster that affects people in Lopburi, my friends and I have helped plant trees at Pasak Chonlasit Dam to alleviate the problem for the past few years. More recently, I was selected to participate in the Young Changemakers Program organized by the School of Changemakers organization. There, I teamed up with my peers to raise awareness about cybercrimes in Thailand. Also, I realized that I’m passionate about applying technologies, including AI, to address social issues. Though I still lack the advanced math and computing background that I believe is a prerequisite for being a great AI developer, I have the willingness to learn and the motivation to excel in whatever I do, as well as my love of helping others.  "With my limited experience in the field of AI, I had a major preconception of what an AI was. I always thought that anything related to AI was daunting and complex. To me, it wasn’t something that a high-schooler would be able to comprehend. However, when I got a chance to work with a professor at KMITL on an image processing project to closely observe a cricket population, my perception of AI has been shifted. In the beginning, I didnt know anything about image processing, so I started studying computer programming and image processing algorithms. Looking back, I was elated that I took on this research journey. I was fortunate that I had a KMITL student and my professor to help me navigate the enormous world of AI. It has been challenging, but rewarding, and I started to believe that I, as a high-schooler, can appreciate the versatility of AI as well. Also, I realized that there is so much more to see in this particular field. So, I decided to apply to this AI Builders program, with a strong determination to learn as much as I can about AI and explore the many ways to use its capability to build something to impact our society. With the guidance from AI experts in this program, I believe I will get to where I set to achieve.",  My inspiration for this project derives from my ongoing work on cricket population surveys using image processing to help farmers keep track of their cricket farms. It led me to wonder about how to assist other farmers in taking care of their livestock. Population counting is just one of the measures of animal well-being, sanitation, and farm productivity. For other animals, there are other measures. For example, recently, there has been a national-level incident involving African Swine Fever, causing deaths in pigs throughout the country and the prices of pork to skyrocket. With early intervention using AI, it may be possible for farms to prevent such catastrophes from happening again. Data for this project can come from live video footage from cameras installed on the farm and sensors that attach to animals to detect anomalies, as well as “cleanliness” sensors at all the gates to assess the farm sanitation."