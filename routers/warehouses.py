from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import crud
import models
import schemas


router = APIRouter()


@router.get(
    "/",
    summary="Retrieve a list of warehouses",
    description="Fetches a paginated list of all warehouses. You can specify `skip` to offset the results and `limit` to control the number of items returned.",
    response_model=list[schemas.Warehouse],
    responses={
        200: {"description": "List of warehouses retrieved successfully"},
        400: {"description": "Invalid pagination parameters"}
    }
)
def read_warehouses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of warehouses from the database.
    Pagination can be controlled with `skip` (offset) and `limit` (max number of results).
    """
    return crud.get_warehouses(db, skip=skip, limit=limit)


@router.post(
    "/",
    summary="Create a new warehouse",
    description="Creates a new warehouse with the provided data.",
    response_model=schemas.Warehouse,
    responses={
        201: {"description": "Warehouse created successfully"},
        400: {"description": "Invalid input data"}
    }
)
def create_warehouse(warehouse: schemas.WarehouseCreate, db: Session = Depends(get_db)):
    """
    Create a new warehouse record in the database.
    This endpoint accepts the warehouse name and location in the body.
    """
    return crud.create_warehouse(db, warehouse=warehouse)


@router.get(
    "/{warehouse_id}",
    summary="Get a warehouse by ID",
    description="Fetches details of a warehouse by its ID.",
    response_model=schemas.Warehouse,
    responses={
        200: {"description": "Warehouse details retrieved successfully"},
        404: {"description": "Warehouse not found"}
    }
)
def read_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the details of a single warehouse using its ID.
    If the warehouse is not found, a 404 error is returned.
    """
    warehouse = crud.get_warehouse(db, warehouse_id=warehouse_id)
    if warehouse is None:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return warehouse


@router.delete(
    "/{warehouse_id}",
    summary="Delete a warehouse",
    description="Deletes a warehouse by its ID.",
    response_model=schemas.Warehouse,
    responses={
        200: {"description": "Warehouse deleted successfully"},
        404: {"description": "Warehouse not found"}
    }
)
def delete_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    """
    Delete a warehouse by its ID. If the warehouse does not exist, a 404 error is returned.
    """
    warehouse = crud.delete_warehouse(db, warehouse_id=warehouse_id)
    if warehouse is None:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return warehouse

