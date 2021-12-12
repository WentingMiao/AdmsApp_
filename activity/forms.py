from django.forms import ModelForm,Textarea,CharField,TextInput,DateInput,EmailInput,Select,PasswordInput,SelectMultiple
from .models import Activity
department_choices = (('publicity','Publicity'),('security','Security'),('entertainment','Entertainment'),('secretary','Secretary'),('volunteer','Volunteer'),('journalist','Journalist'))

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['title','department', 'short_descipt','expected_number','hold_time','post','deadline','registered_members','pic']
        labels ={
            'short_descipt': 'Short description',
            'post': 'Content',
            'pic':'Picture',
            'expected_number':'Expected number of staff',
            'hold_time':'Holding time',
            'registered_members': 'Participants'
        }
        widgets = {  
            
            'department':Select(choices=department_choices,attrs={'class':'form-control'}),
            # 'registered_members':SelectMultiple(attrs={'class':'form-group'}),
        }
        help_texts = {
            'registered_members': 'Press command key to multiselect',
        }
    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if not field_name =='registered_members':
                self.fields[field_name].widget.attrs['class'] = 'form-control'

# class ActivityEditForm():
#     class Meta:
#         model = Activity
#         fields = ['title','department', 'short_descipt','expected_number','hold_time','post','deadline','pic']
#         labels ={
#             'short_descipt': 'Short description',
#             'post': 'Content',
#             'pic':'Picture',
#             'expected_number':'Expected number of staff',
#             'hold_time':'Holding time'
#         }
#         widgets = {
            
           
#             'department':Select(choices=department_choices,attrs={'class':'form-control','placeholder':'department'}),
            
            
#         }