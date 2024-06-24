from PIL import Image, ImageDraw, ImageFont
from dataclasses import dataclass
from uuid import uuid4

@dataclass
class CertificateBuilder:
    """
        CertificateBuilder model for built our certificate
        depends on user inputs.
    """
    bg_img:str
    head:str
    description:str
    client:str
    signer:str

    def build(self) :
        # Open the image
        image = Image.open(f'certificate_builder/certificates/{self.bg_img}.png')

        # Create a drawing object
        draw = ImageDraw.Draw(image)

        # Set the font and size
        BOLD_FONT = ImageFont.truetype("certificate_builder/fonts/Cairo-Bold.ttf", size=90)
        REGULAR_FONT = ImageFont.truetype("certificate_builder/fonts/cairo-regular.ttf", size=90)

        # set the certificate head
        text = self.head
        x, y = 168, 268
        draw.text((x, y), text, font=BOLD_FONT, fill=(255, 255, 255))

        # set the certificate description
        text = self.description
        x, y = 190, 594
        BOLD_FONT.size = 70
        draw.text((x, y), text, font=BOLD_FONT, fill=(162, 167, 174))

        # set the certificate client name
        text = self.client
        x, y = 225, 1244
        BOLD_FONT.size = 110
        draw.text((x, y), text, font=BOLD_FONT, fill=(255, 255, 255))


        # set the certificate signer name
        text = self.signer
        x, y = 1790, 3043
        SIGNER_FONT = ImageFont.truetype("certificate_builder/fonts/signer.ttf", size=139)
        draw.text((x, y), text, font=SIGNER_FONT, fill=(255, 255, 255))

        self.output = "media/outputs/certificate_{0}__{1}.pdf".format(self.client.replace(" ",'_'), uuid4())

        # Save the image
        image = image.convert('RGB')
        image.save(self.output,"PDF")


if __name__ == "__main__" : 
    # Test
    main = CertificateBuilder(
        bg_img='cer_green',
        client="Youssf Ali",
        description="This is my test description",
        head='Certificate for an achivement',
        signer="Mohammed Ali"
    )

    main.build()
    print('saved as : ', main.output)