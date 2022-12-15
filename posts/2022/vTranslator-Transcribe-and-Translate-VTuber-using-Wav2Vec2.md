---
date: "11-7-22"
title: "vTranslator: Transcribe and Translate VTuber using Wav2Vec2"
builder: "ธนภณ ทองจำนงค์ (ธันย์)"
builder_info: ""
thumbnail: "/images/2022/31/01.jpg"
links:
    github: "https://github.com/thunni-noi/vTranslator-prototype"
    facebook: "https://facebook.com/aibuildersx/posts/412504900917955"
    blog: "https://medium.com/@thunninoi/vtranslator-vtuber-speech-recognition-with-wav2vec2-cba2e2c4a6df"
---

![image](/images/2022/31/01.jpg)

- vTranslator คือสคริปต์ที่จะ generate ซับไตเติลของคลิปนั้นๆออกมาเป็นภาษาที่ต้องการ โดยเป็นการรวมกันระหว่างตัว Speech-Recognition Wav2Vec2 และตัว Google Translate เพื่อสร้างไฟล์ซับไตเติล (.srt) ขึ้นมา โดย model Wav2Vec2 ที่นำมาใช้นั้นจะถูก fine-tuned โดยใช้เสียงของ VTuber Hololive เป็นหลัก!,
- แรงบันดาลใจจากการชอบดู VTuber แต่ไม่เข้าใจภาษาญี่ปุ่น ส่วนใหญ่ดูผ่านคนแปลตาม YouTube; อยากดูให้เข้าใจแบบถ่ายทอดสด,
- ชุดข้อมูลหาจากคลิปสั้นๆของ Hololive ข้อดีคือมี timestamp ชัดเจน-ความยาวเหมาะแก่การเทรนโมเดล; ใช้คลิปจากช่องอื่นบางส่วนโดยการทำ OCR ด้วยมือ, "
- ทำความสะอาดช้อมูล เช่น ตัดการใช้อักษร/สัญลักษณ์เพื่ออธิบายสิ่งที่ตัวละครกำลังทำ-ส่วนใหญ่จะไม่มีเสียงพูด ( (^_^), (O.O), ฯลฯ ), สัญลักษณ์แสดงอารมณ์ ( :(, :D, ฯลฯ ), ลบไฟล์เสียงที่เปิดไม่ได้, เปลี่ยนตัวอักษรเป็น hiragana ทั้งหมดด้วย pykakasi",
- ใช้โมเดลพื้นฐาน ได้แก่ vumichien/wav2vec2-large-xlsr-japanese-hiragana (ปรับจูนบน Common Voice และ Japanese speech corpus of Saruwatari-lab) และ ttop324/wav2vec2-live-japanese (ปรับจูนบน Common Voice, JSUT, CSS10, TEDxJP-10K, JVS และ JSS),
- การปรับจูนกับชุดข้อมูล VTuber ทำให้ได้ WER 0.1884

### แรงจูงในในการเข้าร่วมโครงการ (จากใบสมัครเข้าร่วมเมื่อ 10 สัปดาห์ที่แล้ว)

> "ผมเคยเข้าร่วมคอร์สการจัดการข้อมูลโดยใช้ Excel เพื่อหาวิธีการที่มีประสิทธิภาพที่สุด , Data Science เบื้องต้น และการใช้ AI เพื่อสร้างเสียงเสมือน  อยากลองเรียนสายอื่นดูบ้างครับ เพราะตอนนี้เรียนอยู่เป็นเอก DE ที่จะเน้นการจัดการข้อมูลใน Database เป็นหลัก อยากลองทำอย่างอื่นบ้างอะครับ (และก็มาหา Portfolio ไปเผื่อเข้ามหาวิทยาลัยด้วยครับ)  อยากจะทำการประมวลผลภาษาให้ได้ Real-Time เพื่อจะได้ลดช่องว่างระหว่างภาษาและสามารถเข้าใจกันได้ง้ายขึ้น ปัจจุบันก็มีบ้างแล้วแต่ยังไม่แม่นและแพร่หลายขนาดนั้น"