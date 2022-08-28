from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.forms import CarsSearchForm, DriverCreationForm, DriversSearchForm, ManufacturerSearchForm, \
    validate_license_number
from taxi.models import Car, Manufacturer

SEARCH_CAR_URL = reverse("taxi:car-list")


class DriverSearchForm:
    pass


class FormsTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "user",
            "user12345"
        )
        self.client.force_login(self.user)

    def test_driver_creation_with_license_number_first_name_last_name(self):
        form_data = {
            "username": "test_user",
            "license_number": "ABC12345",
            "first_name": "test_firstname",
            "last_name": "test_lastname",
            "password1": "pass1234",
        }
        form = DriverCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_license_number_validation(self):
        self.assertEqual(validate_license_number("ABC12345"), "ABC12345")
        self.assertRegex(validate_license_number("ABC12345"), "^[A-Z]{3}\d{5}$")

    def test_search_fields(self):
        manufacturer = Manufacturer.objects.create(name="Mercedes", country="Germany")
        manufacturer.save()
        car = Car.objects.create(model="S500", manufacturer=manufacturer)
        car.save()

        car_search_form = CarsSearchForm(data={"model": "S"})
        manufacturer_search_form = ManufacturerSearchForm(data={"name": "M"})
        driver_search_form = DriversSearchForm(data={"username": "u"})

        self.assertTrue(car_search_form.is_valid())
        self.assertTrue(manufacturer_search_form.is_valid())
        self.assertTrue(driver_search_form.is_valid())

        self.assertEqual(car_search_form.cleaned_data["model"], "S")
        self.assertEqual(manufacturer_search_form.cleaned_data["name"], "M")
        self.assertEqual(driver_search_form.cleaned_data["username"], "u")
