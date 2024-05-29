
import qrcode
import os


def QrGenerate():
    qr = qrcode.QRCode(version=2,
                   box_size=20,
                   border=5)

    qr.add_data(input("Enter Paste the link for Generate Qr Code : "))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",
              back_color="white")

    filePath  = "E:\Problem_Solving\Projects"
    fileName = input("Enter file Name : ")

    fullFilePath = os.path.join(filePath,fileName + ".png")
    img.save(fullFilePath)   