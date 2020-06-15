#!/usr/bin/env python
#coding=utf-8
#author=guolin
import pytesseract
from PIL import Image
import sys 
reload(sys)
sys.setdefaultencoding( "utf-8")  
# tessdata库：https://github.com/tesseract-ocr/tessdata/

# 先手动下载安装Tesseract-OCR，然后指定tesseract的路径：
pytesseract.pytesseract.tesseract_cmd = 'D:/Program Files (x86)/Tesseract-OCR/tesseract'

# 二值化    
threshold = 140    
table = []    
for i in range(256):    
    if i < threshold:    
        table.append(0)    
    else:    
        table.append(1)
        
def calc():
    image = Image.open(r'f://bcode1.png')
    
    # 转化到灰度图  
    image = image.convert('L')  
      
    # 二值化，采用阈值分割法，threshold为分割点   
    image = image.point(table,'1')    
      
    # 保存转化后的图，方便我们查看效果  
    image.save('f://bcode1_calc.png')  
    
    vcode = pytesseract.image_to_string(image,lang="chi_sim")
    print u'识别出来的内容：',vcode
            
if __name__ == '__main__':
    calc()
    
