---
date: "29-7-22"
title: "RL in Traffic Management"
builder: "ณดล พิพัฒนติกานันท์ (ไตตั้น)"
builder_info: ""
thumbnail: "/images/2022/49.jpg"
links:
github: "https://github.com/nadoltitan/RL_in_Traffic_Management"
facebook: "https://facebook.com/aibuildersx/posts/429097575925354"
blog: "https://medium.com/@nadoltitan1/%E0%B8%A5%E0%B8%94%E0%B8%9B%E0%B8%B1%E0%B8%8D%E0%B8%AB%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%A3%E0%B8%B2%E0%B8%88%E0%B8%A3%E0%B8%95%E0%B8%B4%E0%B8%94%E0%B8%82%E0%B8%B1%E0%B8%94%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-reinforcement-learning-d3b9c6014863"
---

![image](/images/2022/49.jpg)

- โมเดล reinforcement learning (advantage actor-critic; A2C) ทำหรับจัดการไฟจาราจรบนแบบจำลอง Simulation of Urban Mobility (SUMO) ที่สร้างขึ้นมาจากแผนที่จริงผ่าน OpenStreetMap,
- สร้างแบบจำลองแยกจราจรจากแผนที่ OpenStreetMap บน SUMO ด้วยOSMWebWizard; สร้างไฟล์ .net.xml สำหรับเส้นทางเดินรถ และ .rou.xml สำหรับระบุรถที่เข้ามาในเลน กำหนดให้รถเข้ามาในเลนของแบบจำลองโดยการสุ่ม,
- วัดผลโดยการคำนวณความหนาแน่นของรถต่อเลนโดยเฉลี่ย (average lane density),
- ทดลองสี่แยกแบบง่ายกับสถาปัตยกรรม A2C, Deep Q-learning (DQN), Proximal Policy Optimization (PPO); พบว่า A2C ทำได้ดีที่สุด,
- ปัญหาสำคัญของโครงงานนี้ที่ยังต้องหาทางแก้ไข และปรับปรุงต่อไปก็คือ map จากเส้นทางจริงที่ถูก import มาจาก OSM มีความผิดพลาดของเส้นถนนอยู่มากมาย เช่น สัญญาณไฟจราจรที่มีมากกว่าหนึ่งอันในหนึ่งแยก เส้นทางถนนที่เกิดการทับซ้อนกันของ map ทำให้รถวิ่งขวางเส้นทางกันเอง(ซึ่งไม่ควรเกิดขึ้นกับสถานที่จริง) ปัญหาถนนที่เป็นทางตันทำให้รถบางส่วนวิ่งวนและเกิดการติดขัดไปสู่ทั้งระบบ และทำให้เป็นปัญหาในการ import มาให้ RL เรียนรู้ จากปัญหาดังกล่าวทำให้เราตัดสินใจว่า โครงงานนี้จะใช้ map ที่มีอยู่จาก Library SUMO-RL ที่มีความซับซ้อนมากขึ้นและใกล้เคียงกับ map ในสถานที่จริงมากที่สุด แทนการใช้ map ที่มีในสถานที่จริง

### แรงจูงในในการเข้าร่วมโครงการ (จากใบสมัครเข้าร่วมเมื่อ 10 สัปดาห์ที่แล้ว)

> "เราให้นิยามตัวเองว่าเป็นคนที่มีความพยายามต่องานที่ทำอยู่เสมอ จึงมั่นใจได้ว่าเราจะทำโปรเจคนี้อย่างเต็มความสามารถ เรามีความรู้ในการเขียนโปรแกรมภาษา python มาจากการศึกษาด้วยตนเองเพื่อทำ project ในโรงเรียนและมีความกระตือรือร้นที่จะเรียนรู้อีก เรายังได้ทำการศึกษาการเขียนโปรแกรมมาหลากหลายผ่านการเข้าค่ายโอลิมปิกวิชาการคอมพิวเตอร์ค่าย 2 ที่ทำให้เราได้เข้าใจ algorithm ที่หลากหลาย เราได้ร่วมพัฒนาโครงการเครื่องให้อาหารแมวที่ควบคุมบน Web Application และทำงานร่วมกับระบบ IoT โดยตลอดเวลาที่ทำงานเหล่านั้นเราศึกษาบนเว็บต่างประเทศจึงสามารถอ่าน, แปล, และทำความเข้าใจบทความหรือ paper ภาษาอังกฤษได้ดีมาก เรามีแรงบันดาลใจในการสร้าง AI แก้ปัญหาในชีวิตประจำวัน แม้จะเป็นปัญหาเฉพาะกลุ่มแต่ก็สามารถสร้างความแปลกใหม่ได้ เราคาดหวังอย่างยิ่งว่าจะได้รับโอกาสในการทำความฝันนั้นให้เป็นจริง  ปฏิเสธไม่ได้ว่า Artificial Intelligence ได้เข้ามาบทบาทอย่างมากในปัจจุบัน ทั้งช่วยย่นการทำงานของมนุษย์ ช่วยจำแนกหรือวิเคราะห์ข้อมูลที่ซับซ้อน แนะนำ content ที่เกี่ยวข้อง หรือแม้แต่ช่วยตัดสินใจ แต่ก็ใช่ว่า AI จะสามารถทำได้ทุกอย่างหรือแม้แต่การทำงานออกมาได้ perfect 100% ก็เป็นไปได้ยากหากขาด dataset , การจัดการข้อมูลที่ดี หรือ วิธีการ train model ที่เหมาะสม ซึ่งสิ่งนี้จำเป็นต้องศึกษาเพิ่มเติมกว่าความรู้ในม.ปลายไปมาก และจำเป็นต้องพึ่งพาผู้ที่มีประสบการณ์มากกว่า  เราสนใจโครงการ AI Builder ตั้งแต่ปีที่แล้ว แม้จะไม่ผ่านรอบคัดเลือกตัวจริงแต่ก็ได้ศึกษาเนื้อหาไปบ้างในแบบของนักเรียน sit-in หลังจากเห็นโครงงานของเพื่อนหลายคนก็ทำให้เรามีไฟที่อยากจะมาลองสมัครรอบของปีนี้อีก! AI Builder มีเนื้อหาที่เข้มข้นและสิ่งที่สำคัญคือการมี mentor ที่เชี่ยวชาญ และกลุ่มเพื่อนเข้ามาช่วยให้คำปรึกษา เราจึงคิดว่าหากได้เข้าร่วมโครงการนี้แล้ว คงจะได้พัฒนาฝีมือตัวเองให้ดีขึ้นและเข้าใจถึงการพัฒนาโปรเจค AI อย่างเต็มรูปแบบจนอาจสามารถตกตะกอนความรู้และถ่ายทอดให้ผู้อื่นได้ในภายหลัง"