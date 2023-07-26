from django.core.management.base import BaseCommand
from imageutils.models import BlogHeader
from django.core.files.images import get_image_dimensions
import imageutils
import os
class Command(BaseCommand):
    help = 'To Check Dimension of blogheader and send email to Author if dimensions are not valid' 
    def handle(self, *args, **kwargs):
        try:
            # Read a record from DB Table
            record = BlogHeader.objects.filter(dimension_checked=False).first()
            # Get base directory of App
            path = os.path.dirname(imageutils.__file__)
            # Absolute path of image
            imagePath=os.path.join(path,record.image_path)
            self.stdout.write("Reading Dimensions of "+imagePath)
            # Open Image
            image= open(imagePath, 'rb')
            # Get dimensions 
            w, h = get_image_dimensions(image)
            # print dimesnions
            self.stdout.write(" File size:  "+str(w)+"X"+str(h))
            #update record 
            record.dimension_checked = True 
            # Apply logic
            if(w>=450 and w<=600 and h>=450 and h<=600):
                self.stdout.write(" All Good")
                record.has_correct_dimension =True #update record
            else:
                # Dummy Message, In real world we will write logic to send
                # email here
                self.stdout.write(" Email : Hey <User> Please upload a new Image ")
                self.stdout.write(" \t Width should be between 450px and 600px ")
                self.stdout.write(" \t Height should be between 450px and 600px ")
                record.has_correct_dimension =False #update record
            record.save()  #save changes to DB
        except BlogHeader.DoesNotExist:
            self.stdout.write(" No more records. All done  ")
        except FileNotFoundError:    
            self.stdout.write(" File does not exist  ")
      

