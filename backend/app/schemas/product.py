from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponse


class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=200,
                            description="Product name")
    description: Optional[str] = Field(None, description="Product description")