def get_categories():
    return [{
        "id": 1,
        "name": "Iphone"
    }, {
        "id": 2,
        "name": "Macbook"
    }]


def get_products(kw):
    products = [{
        "id": 1,
        "name": "Iphone 20",
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg"
    }, {
        "id": 1,
        "name": "Galaxy 20",
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg"
    }, {
        "id": 1,
        "name": "Iphone 20",
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg"
    }, {
        "id": 1,
        "name": "Galaxy 20",
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg"
    }, {
        "id": 1,
        "name": "Iphone 20",
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg"
    }]

    #if kw:
    #    products = [p for p in products if p["name"].find(kw) >= 0]
    prod = []
    if kw:
        for p in products:
            if p["name"].find(kw) >= 0:
                prod.append(p)

        return prod
    return products
