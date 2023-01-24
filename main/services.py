from .models import Product, Category


def get_categories() -> list:
    return Category.objects.all()


def create_category(data) -> object:
    try:
        category = Category.objects.create(
            name=data.get('name'),
        )

        return category
    except Exception as error:
        pass

    return None


def get_products() -> list:
    return Product.objects.select_related('category').all()


def create_product(data) -> object:
    try:
        product = Product.objects.create(
            name=data.get('name'),
            price=data.get('price'),
            stock=data.get('stock'),
            category_id=data.get('category'),
        )

        return product
    except Exception as error:
        pass

    return None


def get_average_product_price() -> float:
    # TODO
    pass


def get_products_filtered_by_category(category_id: int) -> list:
    # TODO
    pass



