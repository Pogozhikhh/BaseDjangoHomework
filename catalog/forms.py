from django.forms import ModelForm, BooleanField
from .models import Category, Product
from django.core.exceptions import ValidationError


banned_words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_product_name(self):
        product_name = self.cleaned_data.get("product_name")
        for banned_word in banned_words:
            if banned_word in product_name.lower():
                raise ValidationError(
                    f'Слово "{banned_word}" недопустимо в имени товара'
                )
        return product_name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for banned_word in banned_words:
            if banned_word in description.lower():
                raise ValidationError(
                    f'Слово "{banned_word}" недопустимо в описании товара'
                )
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError(f"Цена не должна быть отрицательной")
        return price


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ["is_published"]
