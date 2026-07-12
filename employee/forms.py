from django import forms
from .models import Employee, Leave
import re


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = "__all__"

    # Validate Mobile Number
    def clean_mobile_number(self):
        mobile = self.cleaned_data.get("mobile_number")

        if not re.fullmatch(r"\d{10}", mobile):
            raise forms.ValidationError(
                "Mobile number must contain exactly 10 digits."
            )

        return mobile


class LeaveForm(forms.ModelForm):

    class Meta:
        model = Leave
        fields = "__all__"

    # Validate Dates
    def clean(self):
        cleaned_data = super().clean()

        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        if from_date and to_date:
            if from_date > to_date:
                raise forms.ValidationError(
                    "From Date cannot be greater than To Date."
                )

        return cleaned_data