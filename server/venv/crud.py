from langchain_community.chat_models import ChatOpenAI
from sqlalchemy.orm import Session

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # Add current directory to path
from models import Product

def fetch_product_info(db: Session, query: str):
    return db.query(Product).filter(Product.name.ilike(f"%{query}%")).all()

def chatbot_response(user_query: str, db: Session):
    products = fetch_product_info(db, user_query)
    
    if not products:
        return "No products found."

    product_data = "\n".join([f"{p.name} - {p.brand} (${p.price})" for p in products])
    
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key="your-api-key")
    response = llm.predict(f"Summarize this product data: {product_data}")

    return response
