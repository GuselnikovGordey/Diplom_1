from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        db = Database()
        available_buns = db.available_buns()

        assert available_buns == db.buns

    def test_available_ingredients(self):
        db = Database()
        available_ingredients = db.available_ingredients()

        assert available_ingredients == db.ingredients
