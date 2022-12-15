---
date: "9-8-22"
title: "Find Water from Satellite Images Using U-Net Image Segmentation with Pytorch"
builder: "วรกาญจน์ ลาสุดี (ปีใหม่)"
builder_info: ""
thumbnail: "/images/2022/60/01.jpg"
links:
    github: "https://github.com/19xx47/Find-water-AI-builders-project"
    facebook: "https://facebook.com/aibuildersx/posts/447914850710293"
    blog: "https://medium.com/@worakan.lasudee/found-water-from-satellite-images-by-segmentation-using-u-net-with-pytorch-7b3b0a8abf1d"
---

![image](/images/2022/60/01.jpg)

- โมเดล semantic segmentation สำหรับหาแหล่งน้ำจากรูปถ่ายดาวเทียมโดยใช้ U-Net,
- เทรนบนชุดข้อมูล Satellite Images of Water Bodies จาก Kaggle ซึ่งประกอบด้วยสองประเภทคือ Images และ Mask ซึ่งมีจำนวนข้อมูลทั้งหมด 2841 รูป,
- สถาปัตยกรรม U-net เป็น CNN (convolutional neural networks) ที่แบ่งออกเป็นสองประเภทคือ Encoder และ Decoder ในส่วนของ Encoder เป็นการแปลงขนาดของ Input ให้มีขนาดเล็กลงแต่มี Channel ที่มากขึ้น นั่นคือเครือข่ายสามารถเรียนรู้ ความสัมพันธ์ที่ซับซ้อนได้มากขึ้นในภาพ Decoder มีโครงสร้างสถาปัตยกรรมเหมือนกับ Enconder ซึ่งทำหน้าที่แปลงขนาดภาพให้เป็นขนาดเดิม ใช้ Loss เป็น BCE-Dice Loss,
- เลือกทำ U-net ด้วย Pytorch เพื่อนำมาเปรียบเทียบ U-net ด้วย Tensorflow เพื่อหา Model ที่มีประสิทธิภาพมากที่สุด เนื่องจากทั้งสองตัวต่างก็เป็น deep learning framework ที่เป็นที่นิยมเหมือนกัน แต่ Pytorch นั้นเรียนรู้ได้ง่ายเพราะมี document ที่อ่านได้เข้าใจง่าย มีชุมชนที่ใช้ในงานวิจัยเยอะและมีเครื่องมือ debugging มากมาย ส่วน Tensorflow นั้นแม้จะไม่มี debugging ที่ดีและชุมชนกระตือรือล้นเหมือน Pytorch แต่ Tensorflow เหมาะสำหรับการพัฒนาใน production environment และยังสามารถทำ data visualization ได้ง่ายกว่า Pytorch มาก,
- ทดลอง Optimizer เป็น RMSProp, Adam และ NAdam ด้วย pretrained U-Net จาก Pytorch และ Tensorflow พบว่า Pytorch U-Net และ Adam ทำความแม่นยำระดับ pixel ได้ดีที่สุดที่ 80.7% บน test set

### แรงจูงในในการเข้าร่วมโครงการ (จากใบสมัครเข้าร่วมเมื่อ 10 สัปดาห์ที่แล้ว)

> "ผลงานเกี๋ยวกับ AI 1. Model ทำนายการเสื่อมสภาพของดินเป็นผลให้ได้เป็นตัวแทนเข้าร่วมนำเสนอผลงานที่จัดโดยประเทศเกาหลี 2. Machine Learning ตรวจจับรูปร่างวัตถุโดยใช้กล้องตรวจจับในการแข่งขันหุ่นยนต์ ได้รับรางวัล Control Award และ Winner Award แรงบันดาลใจคือโครงงานที่อยากทำค่ะเป็นผลให้เข้าร่วมกิจกรรมอบรม AI ของ Microsoft และ AWS  ชื่นชอบและสนใจปัยญษประดิษฐ์มากยิ่งเหตุมีข่าวเกี่ยวกับค่าย AI ตั้งแต่ต้นปีก็ตั้งหน้าตั้งตารอวันที่ค่ายเปิดรับสมัครเลยค่ะ หนูเคยเข้าร่วมค่ายวิทยาศาตร์และมีโอกาสได้ทำงานเกี่ยวกับการทำนายของ Model แต่หนูไม่ได้เข้าใจมันทั้งหมดตอนนั้นที่ทำได้เพราะนำโค้ดที่มีอยู่แล้วมาเปลี่ยน dataset แล้วก็แก้นิดหน่อย สิ่งที่หนูจะบอกก็คือหนูอยากเข้าใจกระบวนการ algorithm ของ AI จริงๆค่ะ ถ้าหนูได้เข้าใจ algorithmของAI จริงๆแล้วหนูจะสามารถต่อยอดโครงงานให้เป็นจริงได้ค่ะ  การสร้าง Model วิเคราะห์และบอกประเภทของโรคหัวใจจากเสียงของจังหวะการเต้นและกราฟคลื่นไฟฟ้าของหัวใจโดยใช้การวิเคราะห์เชิงลึก (Big data) ประยุกต์ร่วมกับปัญญาประดิษฐ์ (AI)"