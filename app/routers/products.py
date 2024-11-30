from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import crud
import models
import schemas


router = APIRouter()


@router.get(
    "/",
    summary="Retrieve a list of products",
    description="Fetches a paginated list of all products. You can specify `skip` to offset the results and `limit` to control the number of items returned.",
    response_model=list[schemas.Product],
    responses={
        200: {"description": "List of products retrieved successfully"},
        400: {"description": "Invalid pagination parameters"},
    },
)
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of products from the database.
    Pagination can be controlled with `skip` (offset) and `limit` (max number of results).
    """
    return crud.get_products(db, skip=skip, limit=limit)


@router.post(
    "/",
    summary="Create a new product",
    description="Creates a new product with the provided data, linking it to a specific warehouse.",
    response_model=schemas.Product,
    responses={
        200: {"description": "Product created successfully"},
        400: {"description": "Invalid input data"},
    },
)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """
    Create a new product and associate it with a warehouse.
    This endpoint requires the product name, quantity, and warehouse ID in the body.
    """
    return crud.create_product(db, product=product)


@router.get(
    "/{product_id}",
    summary="Get a product by ID",
    description="Fetches details of a product by its ID.",
    response_model=schemas.Product,
    responses={
        200: {"description": "Product details retrieved successfully"},
        404: {"description": "Product not found"},
    },
)
def read_product(product_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the details of a single product using its ID.
    If the product is not found, a 404 error is returned.
    """
    product = crud.get_product(db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.delete(
    "/{product_id}",
    summary="Delete a product",
    description="Deletes a product by its ID.",
    response_model=schemas.Product,
    responses={
        200: {"description": "Product deleted successfully"},
        404: {"description": "Product not found"},
    },
)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Delete a product by its ID. If the product does not exist, a 404 error is returned.
    """
    product = crud.delete_product(db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
