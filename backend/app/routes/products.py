from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.product_service import ProductService, ProductCreate
from ..schemas.product import ProductResponse, ProductListResponse

router = APIRouter(
    prefix="/api/products",
    tags=["products"]
)

@router.get("", response_model=ProductListResponse, status_code=status.HTTP_200_OK)
def get_products(db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_all_products()

@router.get("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def get_product(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_product_by_id(product_id)

@router.get("/category/{category_id}", response_model=ProductListResponse, status_code=status.HTTP_200_OK)
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_products_by_category(category_id)

@router.post("/create", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_data: ProductCreate, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.create_product(product_data)

@router.put("/update/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product_data: ProductCreate, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.update_product(product_id, product_data)

@router.delete("/delete/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    list = service.delete_product(product_id)
    return list