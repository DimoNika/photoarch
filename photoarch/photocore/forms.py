from django import forms
from .models import UploadFile

class UploadFilesForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = ['file']

    # allowed_extensions = ['.bmp', '.gif', '.jpg', '.jpeg', '.png', '.webp','.mp4', '.webm',  '.ogg']
    def __init__(self, *args, **kwargs):
        super(UploadFilesForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'accept':'.bmp, .gif, .jpg, .jpeg, .png, .webp,.mp4, .webm,  .ogg',
                                                    'multiple': 'multiple',
                                                    'class':'form-control',
                                                    'type':'file',
                                                    'id':'filesform'})
