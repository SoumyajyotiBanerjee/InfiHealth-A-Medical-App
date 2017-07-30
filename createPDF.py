from reportlab.pdfgen import canvas
import time

print 'Enter Dr. Name'
drname = raw_input()
print 'Enter Patient Name'
pname = raw_input()
date = time.strftime("%d/%m/%Y")
file_name = pname+"_prescription_"+date+".pdf"
c = canvas.Canvas("prescription.pdf")
c.drawString(100,800,"Auto Generated Prescription")
c.drawString(100,740,"Dr."+drname)
c.drawString(100,730,"Patient:"+pname+"  Date: "+date)
print 'Enter predicted  disease'
description = raw_input()
c.drawString(100,700,"Disease:"+description)
print 'Enter Number of Medicine'
no_m = int(raw_input())
val = 680
for i in range(0,no_m):
	print 'Enter Medicine name:'
	m_name = raw_input()
	print 'Enter Medicine dosage:'
	d_value = raw_input()
	print 'comments:'
	comments = raw_input()
	c.drawString(100,val,"Medicine:"+m_name+" Dosage:"+ d_value+" comments:"+comments)
	val-=20
c.save()