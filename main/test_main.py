import pytest
from model_bakery.recipe import Recipe

from main import services

generic_product = Recipe(
    "main.Product",
)

generic_category = Recipe(
    "main.Category",
)


@pytest.mark.skip
@pytest.mark.django_db
def test_get_products_filtered_by_category():
    cat1 = generic_category.make()
    cat2 = generic_category.make()
    prod1 = generic_product.make(price=10, category=cat1)
    prod2 = generic_product.make(price=20, category=cat1)
    generic_product.make(price=30, category=cat2)

    result = services.get_products_filtered_by_category(category_id=cat1.id)

    assert result == [prod1, prod2]


@pytest.mark.skip
@pytest.mark.django_db
def test_get_average_product_price():
    generic_product.make(price=10)
    generic_product.make(price=20)
    generic_product.make(price=30)
    assert services.get_average_product_price() == 20.0


# TODO rendalo: un test un poco más complejo de python a secas


@pytest.mark.django_db
def test_product_list_view(client):
    prod1 = generic_product.make(
        name="prod1",
        price=10,
        stock=2,
        category=generic_category.make(name="cat1"),
    )
    response = client.get("/main/products/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": prod1.id,
            "name": "prod1",
            "price": 10,
            "stock": 2,
            "category": {
                "id": prod1.category.id,
                "name": "cat1",
            }
        }
    ]


# TODO rendalo: test crear producto
@pytest.mark.django_db
def test_create_product_api_view(client):
    category = generic_category.make(name="category1")

    response = client.post(
        "/main/products/",
        {
            "name": "product1",
            "price": 200,
            "stock": 20,
            "category": category.id
        },
        format='json'
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 1,
        "name": "product1",
        "price": 200,
        "stock": 20,
        "category": {
            "id": category.id,
            "name": category.name,
        }
    }

# TODO postulante: test en algo que use todo


@pytest.mark.django_db
def test_get_product_api_view(client):
    product = generic_product.make(
        name="product1",
        price=100,
        stock=200,
        category=generic_category.make(name="category1"),
    )

    response = client.get('/main/products/{0}/'.format(product.pk))

    assert response.status_code == 200

    assert response.json() == {
        "id": product.id,
        "name": "product1",
        "price": 100,
        "stock": 200,
        "category": {
            "id": product.category.id,
            "name": "category1",
        }
    }


@pytest.mark.django_db
def test_edit_product_api_view(client):
    product = generic_product.make(
        name="product1",
        price=100,
        stock=200,
        category=generic_category.make(name="category1"),
    )

    response = client.put(
        '/main/products/{0}/'.format(product.pk),
        {
            "name": "product1",
            "price": 100,
            "stock": 150,
            "category": product.category.pk
        },
        content_type='application/json'
    )

    assert response.status_code == 200

    assert response.json() == {
        "id": product.id,
        "name": "product1",
        "price": 100,
        "stock": 150,
        "category": {
            "id": product.category.id,
            "name": "category1",
        }
    }


@pytest.mark.django_db
def test_delete_product_api_view(client):
    product = generic_product.make(
        name="product1",
        price=100,
        stock=200,
        category=generic_category.make(name="category1"),
    )

    response = client.delete(
        '/main/products/{0}/'.format(product.pk),
    )

    assert response.status_code == 202

    assert response.json() == {
        "product_id": product.id,
    }
