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


def get_product(product_id) -> object:
    try:
        return Product.objects.select_related('category').get(pk=product_id)
    except (Product.DoesNotExist, Product.MultipleObjectsReturned) as error:
        pass

    return None


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


def edit_product(product_id, data) -> object:
    try:
        product = get_product(product_id)

        product.name = data.get('name')
        product.price = data.get('price')
        product.stock = data.get('stock')
        product.category_id = data.get('category')
        product.save()

        return product
    except Exception as error:
        pass

    return None


def delete_product(product_id) -> object:
    try:
        product = get_product(product_id)

        product_id = product.pk

        product.delete()

        return product_id
    except Exception as error:
        pass

    return None


def get_average_product_price() -> float:
    # TODO
    pass


def get_products_filtered_by_category(category_id: int) -> list:
    # TODO
    pass
