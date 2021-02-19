from django.db import migrations


def forwards_func(apps, schema_editor):
    serv_cat_model = apps.get_model("mainapp", "ServicesCategory")  # Load model for make changes
    serv_model = apps.get_model("mainapp", "Services")  # Load model for make changes
    con_model = apps.get_model("mainapp", "Contacts")  # Load model for make changes
    home_news_model = apps.get_model("mainapp", "News")
    home_benefits_model = apps.get_model("mainapp", "Benefits")
    home_team_model = apps.get_model("mainapp", "Team")

    # Create new category
    serv_cat_obj = serv_cat_model.objects.create(
        pk=1,
        name="Ground",
        name_long="Ground shipping",
        desc_category="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam",
    )
    # Create new products in this category
    serv_model.objects.create(
        pk=1,
        category=serv_cat_obj,  # Foreign key
        name="Gazel NEXT",
        image="services_images/gazel.jpg",
        description="The reliability of the vehicle has been tested and confirmed by bench, forced and long-term road tests using special methods",
        lifting="5 tons",
        price="100.00",
        quantity=100,
    )
    serv_model.objects.create(
        pk=2,
        category=serv_cat_obj,  # Foreign key
        name="Volvo FE350",
        image="services_images/volvo_5.jpg",
        description="The new generation of Volvo FL distribution trucks for intercity and short regional transport road tests using special methods",
        lifting="10 tons",
        price="1000.00",
        quantity=20,
    )
    serv_model.objects.create(
        pk=3,
        category=serv_cat_obj,  # Foreign key
        name="Volvo FH550",
        image="services_images/volvo_10.jpg",
        description="New generation features offered in the FH versions and the flagship FH16: a completely new, more spacious and comfortable",
        lifting="40 tons",
        price="10000.00",
        quantity=10,
    )
    del serv_cat_obj  # Delete link for category

    # Create new category
    serv_cat_obj = serv_cat_model.objects.create(
        pk=2,
        name="Railway",
        name_long="Railway shipping",
        desc_category="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam",
    )

     # Create new products in this category
    serv_model.objects.create(
        pk=4,
        category=serv_cat_obj,  # Foreign key
        name="«Tornado» № 60163",
        image="services_images/railway_1.jpg",
        description="The reliability of the vehicle has been tested and confirmed by bench, forced and long-term road tests using special methods",
        lifting="5 tons",
        price="100.00",
        quantity=100,
    )
    serv_model.objects.create(
        pk=5,
        category=serv_cat_obj,  # Foreign key
        name="EMD SD40-2",
        image="services_images/railway_2.jpg",
        description="The reliability of the vehicle has been tested and confirmed by bench, forced and long-term road tests using special methods",
        lifting="5 tons",
        price="100.00",
        quantity=100,
    )
    serv_model.objects.create(
        pk=6,
        category=serv_cat_obj,  # Foreign key
        name="Siemens ES64U4",
        image="services_images/railway_3.jpg",
        description="The reliability of the vehicle has been tested and confirmed by bench, forced and long-term road tests using special methods",
        lifting="5 tons",
        price="100.00",
        quantity=100,
    )

    del serv_cat_obj  # Delete link for category

    # Create new category
    serv_cat_obj = serv_cat_model.objects.create(
        pk=3,
        name="Water",
        name_long="Water shipping",
        desc_category="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam",
    )

     # Create new products in this category
    serv_model.objects.create(
        pk=7,
        category=serv_cat_obj,  # Foreign key
        name="ТRPКСN project 941",
        image="services_images/water_1.jpg",
        description="The reliability of the vehicle has been tested and confirmed by bench, forced and long-term road tests using special methods",
        lifting="5 tons",
        price="100.00",
        quantity=100,
    )
    serv_model.objects.create(
        pk=8,
        category=serv_cat_obj,  # Foreign key
        name="ROPAX",
        image="services_images/water_2.jpg",
        description="The reliability of the vehicle has been tested and confirmed by bench, forced and long-term road tests using special methods",
        lifting="5 tons",
        price="100.00",
        quantity=100,
    )
    serv_model.objects.create(
        pk=9,
        category=serv_cat_obj,  # Foreign key
        name="Aurelia K",
        image="services_images/water_3.jpg",
        description="The reliability of the vehicle has been tested and confirmed by bench, forced and long-term road tests using special methods",
        lifting="5 tons",
        price="100.00",
        quantity=100,
    )
    del serv_cat_obj  # Delete link for category

    # Create new category
    serv_cat_obj = serv_cat_model.objects.create(
        pk=4,
        name="Air",
        name_long="Air shipping",
        desc_category="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam",
    )

     # Create new products in this category
    serv_model.objects.create(
        pk=10,
        category=serv_cat_obj,  # Foreign key
        name="Ан-225",
        image="services_images/air_3.jpg",
        description="The reliability of the vehicle has been tested and confirmed by bench, forced and long-term road tests using special methods",
        lifting="5 tons",
        price="100.00",
        quantity=100,
    )
    serv_model.objects.create(
        pk=11,
        category=serv_cat_obj,  # Foreign key
        name="MD-11",
        image="services_images/air_2.jpg",
        description="The reliability of the vehicle has been tested and confirmed by bench, forced and long-term road tests using special methods",
        lifting="5 tons",
        price="100.00",
        quantity=100,
    )
    serv_model.objects.create(
        pk=12,
        category=serv_cat_obj,  # Foreign key
        name="Ju-290А-7",
        image="services_images/air_1.jpg",
        description="The reliability of the vehicle has been tested and confirmed by bench, forced and long-term road tests using special methods",
        lifting="5 tons",
        price="100.00",
        quantity=100,
    )

    # Create news
    home_news_model.objects.create(
        pk=1,
        title="News title",
        text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing",
        public_date="2021-02-08T01:28:07Z",
    )
    home_news_model.objects.create(
        pk=2,
        title="News title",
        text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing",
        public_date="2021-02-08T01:28:07Z",
    )

    # Create contacts
    con_model.objects.create(
        pk=1, city="Moscow", phone="+7 (999) 999-99-99", email="lshop@logistic.com", address="st. Tverskaya 100"
    )
    con_model.objects.create(
        pk=2,
        city="Ekaterinburg",
        phone="+7 (999) 999-99-99",
        email="shop-ekb@logistic.com",
        address="st. Pushkinskaya 50",
    )
    con_model.objects.create(
        pk=3, city="Izhevsk", phone="+7 (999) 999-99-99", email="lshop-izh@logistic.com", address="st. Udmurtskaya 200"
    )

    # Create benefits
    home_benefits_model.objects.create(
        pk=1, title="Safety", desc="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod"
    )
    home_benefits_model.objects.create(
        pk=2,
        title="High quality drivers",
        desc="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod",
    )
    home_benefits_model.objects.create(
        pk=3,
        title="Guarantee & Support 24/7",
        desc="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod",
    )
    home_benefits_model.objects.create(
        pk=4,
        title="Personal manager",
        desc="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod",
    )

    # Create team
    home_team_model.objects.create(
        pk=1,
        full_name="John Smith",
        profession="Logistic manager - 8 years experience",
        photo="team_photo/team1.jpg",
        email="john@centerlogistic.com",
        phone="+987412512543",
    )
    home_team_model.objects.create(
        pk=2,
        full_name="Daniel Kore",
        profession="Software engineer",
        photo="team_photo/team2.jpg",
        email="daniel@centerlogistic.com",
        phone="+987423252253",
    )
    home_team_model.objects.create(
        pk=3,
        full_name="John Smith",
        profession="Marketing specialist - 10 years experience",
        photo="team_photo/team3.jpg",
        email="anna@centerlogistic.com",
        phone="+98735353456",
    )


def reverse_func(apps, schema_editor):
    serv_cat_model = apps.get_model("mainapp", "ServicesCategory")  # Load model for make changes
    con_model = apps.get_model("mainapp", "Contacts")  # Load model for make changes
    home_news_model = apps.get_model("mainapp", "News")
    home_benefits_model = apps.get_model("mainapp", "Benefits")
    home_team_model = apps.get_model("mainapp", "Team")

    # Delete all objects
    serv_cat_model.objects.all().delete()
    con_model.objects.all().delete()
    home_news_model.objects.all().delete()
    home_benefits_model.objects.all().delete()
    home_team_model.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [("mainapp", "0001_initial")]
    operations = [migrations.RunPython(forwards_func, reverse_func)]
