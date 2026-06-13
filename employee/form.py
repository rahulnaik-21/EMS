from django.forms import ModelForm
from .models import Employee,Department
from django import forms
class EmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
    def clean_salary(self):

        salary = self.cleaned_data[
            'salary'
        ]

        if salary <= 0:

            raise forms.ValidationError(
                'Salary must be positive'
            )

        return salary


class DepartmentForm(ModelForm):

    class Meta:
        model = Department
        fields = '__all__'