from fastapi import APIRouter, Depends, Request
from app.catalog.application.dto.CreateProduct import ProductCreateDTO
from app.catalog.application.dto.UpdateProduct import ProductUpdateDTO
from app.catalog.application.mapper.Product import ProductMapper as mapper
from app.catalog.domain.repository.IProduct import IRepository
from app.catalog.infraestructure.logger.logger import saveAnymousLog as log
from app.catalog.infraestructure.repository.Product import Repository as repository
from app.catalog.domain.service.Product import ProductService as service
from app.catalog.infraestructure.shared.account import get_current_user
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/products/create", tags=["products"])
def create(data : ProductCreateDTO ,repository: IRepository = Depends(repository), current_user = Depends(get_current_user)):
    product = mapper.fromDtoToDomain(data)

    if service.find(repository=repository, id=product.id) or service.find_by_sku(repository=repository, sku=product.sku):
        return JSONResponse(status_code=404, content={"detail": "the product already exist"})
    
    service.create(repository=repository, product=product)
    return JSONResponse(status_code=200, content={"detail": "the product was created"})

@router.get("/products", tags=["products"])
def list(page: int = 1, ip: str = 0, repository: IRepository = Depends(repository)):
    catalog = service.list(repository=repository, page=page)
    response = mapper.fromDomainListToDtoList(catalog)
    total = service.total(repository=repository)

    if ip:
        log(ip=ip, data=response)

    return {"detail": { "list" : response, "total": total}}

@router.delete("/products/{product_id}", tags=["products"])
def delete(product_id: int ,repository: IRepository = Depends(repository), current_user = Depends(get_current_user)):
    
    if not service.find(repository=repository, id=product_id):
        return JSONResponse(status_code=404, content={"detail": "the product does not exist"})

    service.delete(repository=repository, id=product_id)
    return JSONResponse(status_code=200, content={"detail": "the product with id " + str(product_id) + " was deleted"})

@router.put("/products/update", tags=["products"])
def update(data: ProductUpdateDTO ,repository: IRepository = Depends(repository), current_user = Depends(get_current_user)):

    product = mapper.fromDtoToDomain(data)

    if not service.find(repository=repository, id=product.id):
        return JSONResponse(status_code=404, content={"detail": "the product does not exist"})

    service.update(repository=repository, product=product)
    return JSONResponse(status_code=200, content={"detail": "the product was updated"})