from allauth.account.forms import (LoginForm,
                                   ResetPasswordForm,
                                   ResetPasswordKeyForm)


class CustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):
        # insert stuff here
        for fieldname, field in self.fields.items():
            if fieldname == ('input') or ('TextInput'):
                field.widget.attrs.update({
                    "class": "input-field"
                    })
            elif fieldname == "label":
                field.widget.attrs.update({
                    "class": "input-label"
                    })
            else:
                pass

        return super(CustomLoginForm, self).login(*args, **kwargs)


class CustomResetPasswordForm(ResetPasswordForm):

    def save(self, request):

        # insert stuff
        email_address = super(CustomResetPasswordForm, self).save(request)
        for fieldname, field in self.fields.items():
            if fieldname == ('input') or ('TextInput'):
                field.widget.attrs.update({
                    "class": "input-field"
                    })
            elif fieldname == "label":
                field.widget.attrs.update({
                    "class": "input-label"
                    })
            else:
                pass

        return email_address


class CustomResetPasswordKeyForm(ResetPasswordKeyForm):

    # override save on password reset form

    def save(self):

        # insert stuff here

        super(CustomResetPasswordKeyForm, self).save()




