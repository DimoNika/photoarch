from django import forms
from .models import UploadFile

class UploadFilesForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = ['file']
    
    def __init__(self, *args, **kwargs):
        super(UploadFilesForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'accept':'.jpg,.jpeg,.png,.gif',
                                                    'multiple': 'multiple'})