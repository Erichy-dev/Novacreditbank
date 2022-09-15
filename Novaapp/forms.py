from Novaapp.models import Portfolio
from django import forms



class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ("ben_name", "account_number"
        )