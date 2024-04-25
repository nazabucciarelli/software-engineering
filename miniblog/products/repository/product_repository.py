from typing import (
    Optional,
    List
)
from products.models import (
    Product,
    Category
)

class ProductRepository:
    def create(self,
               name: str,
               price: float,
               stock: int,
               description: Optional[str] = None,
               category: Optional[Category] = "Sin descripción"
               ) -> Product:
        return Product.objects.create(
            name=name,
            description=description,
            price=price,
            category=category,
            stock=stock,
        )
    
    def get_all(self) -> List[Product]:
        return Product.objects.all()
    
    def get_by_id(self,id) -> Optional[Product]:
        try: 
            return Product.objects.get(id=id)
        except:
            print(f"Product with id {id} not found")

    def get_product_on_price_range(
            self,
            min_price: float,
            max_price: float
    ) -> List[Product]:
        return Product.objects.filter(
            price__range = (min_price,max_price)
        )
    
    def get_product_by_category_id(
            self,
            category_id) -> List[Product]:
        return Product.objects.filter(category=category_id)
