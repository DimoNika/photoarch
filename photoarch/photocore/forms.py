from django import forms
from .models import UploadFile

class UploadFilesForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = ['file']
    
    def __init__(self, *args, **kwargs):
        super(UploadFilesForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'accept':'.3gp,.avi,.mov,.m4v,.m4a,.mp3,.mkv,.ogm,.ogg,.oga,.webm,.wav,.bmp,.gif,.jpg,.jpeg,.png,.webp',
                                                    'multiple': 'multiple',
                                                    'class':'form-control',
                                                    'type':'file',
                                                    'id':'filesform'})
