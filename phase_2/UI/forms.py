from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'id_number','description', 'header', 'tester',
                  'date', 'urgency', 'types', 'test_object',
                  'version', 'remarks')
   
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.fields: 
            self.fields[field].widget.attrs['class'] = 'form-control'            
        self.fields['name'].required = False
        self.fields['urgency'].required = False
        self.fields['tester'].required = False
        self.fields['types'].required = False
        self.fields['test_object'].required = False
        self.fields['version'].required = False