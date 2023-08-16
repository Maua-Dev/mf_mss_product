import pytest
from src.shared.domain.entities.order_products import OrderProducts
from src.shared.helpers.errors.domain_errors import EntityError


class Test_OrderProducts:
    def test_order_products(self):
        order_product = OrderProducts(
            product_name="Saladinha",
            product_id="305c486c-ce77-423d-97c1-1710a4c302da",
            quantity=2
        )

        assert type(order_product) == OrderProducts
        assert order_product.product_name == "Saladinha"
        assert order_product.product_id == "305c486c-ce77-423d-97c1-1710a4c302da"
        assert order_product.quantity == 2

    def test_invalid_product_name(self):
        with pytest.raises(EntityError):
            order_product = OrderProducts(
                product_name=True,
                product_id="305c486c-ce77-423d-97c1-1710a4c302da",
                quantity=2
        )
            
    def test_invalid_product_id(self):
        with pytest.raises(EntityError):
            order_product = OrderProducts(
                product_name="Saladinha",
                product_id=32,
                quantity=2
        )
            
    def test_wrong_length_product_id(self):
        with pytest.raises(EntityError):
            order_product = OrderProducts(
                product_name="Saladinha",
                product_id="305c486c-ce77-423d-97c1",
                quantity=2
        )
    
    def test_invalid_quantity(self):
        with pytest.raises(EntityError):
            order_product = OrderProducts(
                product_name="Saladinha",
                product_id="305c486c-ce77-423d-97c1-1710a4c302da",
                quantity="2"
        )
            
    def test_negative_quantity(self):
        with pytest.raises(EntityError):
            order_product = OrderProducts(
                product_name="Saladinha",
                product_id="305c486c-ce77-423d-97c1-1710a4c302da",
                quantity=-2
        )