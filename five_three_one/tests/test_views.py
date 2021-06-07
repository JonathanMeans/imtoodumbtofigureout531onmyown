from django.test import TestCase
from django.utils.html import escape

from five_three_one.forms import TrainingMaxForm, NewLiftForm
from five_three_one.models import Lift


class TestHomeView(TestCase):
    def test_uses_home_template(self) -> None:
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_uses_tmax_form(self) -> None:
        response = self.client.get("/")
        self.assertIsInstance(response.context["form"], TrainingMaxForm)

    def test_uses_new_lift_form(self) -> None:
        response = self.client.get("/")
        self.assertIsInstance(response.context["new_lift_form"], NewLiftForm)

    def test_POST_uses_tmax_form(self) -> None:
        response = self.client.post("/", data={"training_max": "170"})
        self.assertIsInstance(response.context["form"], TrainingMaxForm)

    def test_error_on_alpha_tmax(self) -> None:
        response = self.client.post(
            "/", data={"training_max": "abc", "week_number": "1"}
        )
        self.assertIn("Enter a number", response.context["errors"]["training_max"][0])

    def test_error_on_too_small_tmax(self) -> None:
        response = self.client.post(
            "/", data={"training_max": "50", "week_number": "1"}
        )
        self.assertIn(
            "greater than or equal to", response.context["errors"]["training_max"][0]
        )

    def test_POST_uses_home_template(self) -> None:
        response = self.client.post("/", data={"training_max": "170"})
        self.assertTemplateUsed(response, "home.html")

    def test_POST_shows_deadlift_workout(self) -> None:
        response = self.client.post(
            "/", data={"training_max": "425", "week_number": "1"}
        )
        self.assertContains(response, "40%")
        self.assertContains(response, "5")
        self.assertContains(response, "170")
        self.assertContains(response, "45x1")

    def test_POST_exercise_redirects_to_lifts(self) -> None:
        response = self.client.post(
            "/save", data={"training_max": "425", "name": "Deadlift"}
        )
        self.assertRedirects(response, "/lifts")

    def test_POST_exercise_adds_to_db(self) -> None:
        self.client.post(
            "/save", data={"training_max": "425", "name": "Deadlift", "week_number": 1}
        )
        self.assertEqual(1, Lift.objects.count())
        lift = Lift.objects.first()
        self.assertEqual("Deadlift", lift.name)
        self.assertEqual(425, lift.training_max)


class TestLiftsView(TestCase):
    def test_lifts_page_uses_lifts_template(self) -> None:
        response = self.client.get("/lifts")
        self.assertTemplateUsed(response, "lifts.html")

    def test_lifts_page_shows_added_lifts(self) -> None:
        Lift.objects.create(name="Deadlift", training_max=425, week_number=1)
        response = self.client.get("/lifts")
        self.assertContains(response, "Deadlift")

    def test_lift_links_to_specific_lift_page(self) -> None:
        Lift.objects.create(name="Deadlift", training_max=425, week_number=2)
        response = self.client.get("/lifts")
        self.assertContains(response, escape("/lift?training_max=425&week_number=2"))


class TestLiftView(TestCase):
    def test_lift_page_uses_lift_template(self) -> None:
        response = self.client.get("/lift")
        self.assertTemplateUsed(response, "lift.html")

    def test_lift_page_shows_workout(self) -> None:
        response = self.client.get(
            "/lift", data={"training_max": "425", "week_number": "1"}
        )
        self.assertContains(response, "40%")
        self.assertContains(response, "5")
        self.assertContains(response, "170")
        self.assertContains(response, "45x1")
