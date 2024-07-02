from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory storage for recipes (replace with database later)
recipes = []

class Ingredient(BaseModel):
    name: str
    amount: str

class Recipe(BaseModel):
    id: Optional[int] = None
    name: str
    ingredients: List[Ingredient]
    instructions: str

@app.post("/recipes/", response_model=Recipe)
async def create_recipe(recipe: Recipe):
    recipe.id = len(recipes) + 1
    recipes.append(recipe)
    return recipe

@app.get("/recipes/{recipe_id}", response_model=Recipe)
async def get_recipe(recipe_id: int):
    if recipe_id < 1 or recipe_id > len(recipes):
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipes[recipe_id - 1]

@app.get("/recipes/", response_model=List[Recipe])
async def list_recipes():
    return recipes

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
