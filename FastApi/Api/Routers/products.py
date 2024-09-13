from fastapi import APIRouter

router_prods = APIRouter(
    prefix="/products", tags=["products"], responses={404: {"msg": "no encontrado"}}
)


prod_list = ["producto1", "producto2", "producto3", "producto4"]


@router_prods.get("/")
async def get_products():
    return prod_list


@router_prods.get("/{id}")
async def get_products(id: int):
    return prod_list[id]
