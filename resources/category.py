from flask import request
from flask_restful import Resource
from model import db, Category, CategorySchema

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


class CategoryResource(Resource):

    def get(self):
        """
        this is the category list api endpoint. Used for GET requests only
        """
        categories = Category.query.all()
        categories = categories_schema.dump(categories).data
        return {"status": "success", "data": categories}, 200

    def post(self):
        """
        Create new category endpoint - POST requests.
        """
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No input data provided"}, 400

        # get data from json, check for errors
        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422
        category = Category.query.filter_by(name=data['name']).first()
        if category:
            return {"message": "Category already exists"}, 400
        category = Category(name=json_data['name'])

        db.session.add(category)
        db.session.commit()

        result = category_schema.dump(category).data

        return {"status": "success", "data": result}, 201

    def put(self):
        """
        Update existing category (id).
        """
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No input data provided"}, 400

        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422
        category = Category.query.filter_by(id=data['id']).first()
        if not category:
            return {"message": "Category does not exist"}, 400
        category.name = data['name']
        db.session.commit()

        result = category_schema.dump(category).data
        return {"status": "success", "data": result}, 204

    def delete(self):
        """
        Delete existing category (id).
        """
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No input data provided"}, 400

        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422
        category = Category.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = category_schema.dump(category).data
        return {"status": "success", "data": result}, 204
