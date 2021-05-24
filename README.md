# SourceSage Full Stack Developer Challenge

> This repository contains the challenge for full stack developers.

- [Devops Exercise](#devops-exercise)
- [Backend Exercise](#backend-exercise)
- [Frontend Exercise](#frontend-exercise)

## Devops Exercise

The backend and frontend exercises should be contained in one repository (monorepo), with the following directory layout:

```bash
├── backend
├── frontend
├── docker-compose.yml
└── README.md # documentation for this repo
```

The `backend` and `frontend` directories should have their own simple `Dockerfile`, so that they can be built and run individually.

The `docker-compose.yml` file should define both the `backend` and `frontend` as services, which will be automatically built and started upon calling `docker-compose up`. A container for a DB can be defined here as well.

## Backend Exercise

The project should be made available in the `backend` directory with meaningful commit messages. Use flask and if needed, any supporting framework.

Implement a **simple REST API** to **manage** "Products" and "Variants".

The "Products" resource should have the following properties:

- id: any type of unique id
- name: name of the product
- description: description of the product
- images: an list of associated images
- logo_id: the primary logo for this images
- created_at: timestamp
- updated_at: timestamp

The "Variants" resource should have the following properties:

- id: any type of unique id
- product_id: id of the relevant product
- name: name of the variant
- size: size of the variant
- color: color of the variant
- images: an list of associated images
- created_at: timestamp
- updated_at: timestamp

The "Image" resource can have the following properties:

- id: any type of unique id
- url: the url of the image

The apis you build must be able to accomplish the following tasks:
1. Create/Update a product
2. Create multiple variants under a product
3. Update a variant
4. Link Products/Variants to images
5. Query products and variants

The data should be stored in a MySQL database.

## Frontend Exercise

The project should be made available in a the `frontend` directory with meaningful commit messages. You should build it using ReactJS.

Implement a simple dashboard that has the following pages:

1. A page to list all products.
2. A page to create a product.
3. A page to create a variant under a product.
4. A page view a product and its variants.

Please use [Ant Design](https://ant.design/) to style your frontend.