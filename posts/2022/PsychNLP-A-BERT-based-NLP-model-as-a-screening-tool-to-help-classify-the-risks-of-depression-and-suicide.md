---
date: "6-8-22"
title: "PsychNLP: A BERT-based NLP model as a screening tool to help classify the risks of depression and suicide"
builder: "พลกฤต สาตสิน (เจ)"
builder_info: ""
thumbnail: "/images/2022/57/01.jpg"
links:
    github: "https://github.com/urseamajoris/PsychNLP"
    facebook: "https://facebook.com/aibuildersx/posts/441008288067616"
    blog: "https://medium.com/@urseamlaccs/psychnlp-part-1-d8180740c0ec"
---

![image](/images/2022/57/01.jpg)

- โมเดลแยกแยะข้อความ depression, suicidal และ neither จากข้อความในกระทู้ออนไลน์; อยู่ในขั้นตอนการศึกษา ไม่สามารถนำไปวินิฉัยโรคได้จริง โปรดใช้วิจารณญาณในการรับชม,
- แรงบันดาลใจจากจับใจและสายใจ บอทคัดกรองภาวะซึมเศร้าของโรงพยาบาลศิริราช,
- เก็บข้อมูลจากกระทู้ Reddit ที่มีข้อความยาวกว่า 32 ตัวอักษรต่อประโยคด้วย Python Reddit API Wrapper (PRAW) และ PushshiftAPI รวมประมาณ 400,000 ประโยค; ทำความสะอาดด้วยการลบ emoticon, ปรับเป็น lowercase, ลบสัญลักษณ์ต่างๆ ฯลฯ,
- แยก label ตาม subreddit คือ depression จาก r/depression, suicidal จาก r/SuicideWatch และ neither จาก r/offmychest (คนมาโพสระบายเฉยๆไม่ได้ระบุว่าต้องมีอาการ); มีจำนวนแต่ละ label เท่าๆกัน,
- ปรับจูนสถาปัตยกรรม all-distilroberta-v1 ที่เป็น sentence embeddings (768 dimensions) แล้วเพิ่ม classification head เพื่อจำแนกประเภทข้อความ,
- ได้ผลใกล้เคียงกับ baseline ที่เป็น tf-idf + LinearSVC ที่ F1 0.548 (vs 0.584) และ accuracy 62.7% (vs 58.8%),
- จากการวิเคราะห์พบว่าสาเหตุใหญ่มาจากข้อความใน r/depression และ r/SuicideWatch มีความคล้ายคลึงกันแม้ตัดสินด้วยมนุษย์,
- สามารถปรับไปใช้กับ Discord Bot ได้ด้วย

### แรงจูงในในการเข้าร่วมโครงการ (จากใบสมัครเข้าร่วมเมื่อ 10 สัปดาห์ที่แล้ว)

> "ผมสนใจแพทยศาสตร์เป็นหลัก และตอนนี้ AI ก็มีความน่าสนใจเท่ากัน ผมเคยศึกษางานวิจัยจากรามาธิบดีเวชสารมาพอสมควร และพบว่า ยังมีสิ่งที่ผมสามารถต่อยอดจากการเอาทั้ง 2 แขนงมารวมกันได้อีกมาก ผมได้กล่าวไปในจดหมายที่ส่งให้คณะแพทยศาสตร์โรงพยาบาลรามาธิบดี และผมจะกล่าวไว้ที่นี่เช่นกัน ว่าผมมีจุดมุ่งหมายจะนำทั้ง 2 แขนงนี้มาสร้างประโยชน์ให้สังคม นี่เป็นเหตุที่ผมตัดสินใจสมัคร AI Builders และเป็นเหุผลที่ท่านควรรับผมเข้าโครงการครับ  เมื่อช่วง lockdown ปี 2564 ผมมาเริ่มสนใจการเขียนโปรแกรม เริ่มเรียน python ด้วยตัวเองประมาณ 2 เดือน ต่อมาเห็นเพื่อนที่เรียนมาด้วยกันทำโครงงาน CNN พยากรณ์อาการลมชักจากสัญญาณ EEG ผมก็เลยเข้ามาสนใจในงาน AI มากขึ้น ใช้เวลาอีก 2 เดือนเรียน Tensorflow จนพอมีพื้นฐานบ้าง แต่ผมเรียนทุกอย่างด้วยตัวเอง ไม่เคยได้มีโอกาสที่ได้รับหลักสูตรในสายนี้จาก Lectures เลย ผมเห็นว่า AI Builders เป็นโอกาสให้ผมได้มีประสบการณ์ในด้าน AI อย่างเป็นทางการ ให้ผมได้เรียนรู้และพบปะคนอื่นที่มีความสนใจตรงกับผม และทำ projects เพื่อเพิ่มประสบการณ์ที่จะกลับมาพัฒนาในสิ่งที่เป็นประโยชน์สูงสุดครับ"