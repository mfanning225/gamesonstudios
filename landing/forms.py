from django import forms
from .models import Landing

class LandingForm(forms.ModelForm):

    class Meta:
        model = Landing
        fields = ['name', 'email']\

    def __init__(self, *args, **kwargs):
        super(LandingForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

            self.fields['name'].widget.attrs.update({'id':'floatingInput'})
            self.fields['email'].widget.attrs.update({'id':'floatingPassword'})


        #   <div class="form-floating mb-3">
        #     <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
        #     <label for="floatingInput">{{contact_us.label}}</label>
        #   </div>
        #   <div class="form-floating">
        #     <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
        #     <label for="floatingPassword">{{contact_us.label}}</label>
        #   </div>