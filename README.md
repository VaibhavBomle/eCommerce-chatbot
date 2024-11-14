# eCommerce-chatbot
# eCommerce Chatbot

An AI-driven e-commerce chatbot that offers personalized product recommendations and responds to customer queries based on product reviews and titles. Built using advanced embeddings and language models, this chatbot provides an engaging and helpful shopping assistant experience.

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Setup](#setup)

---

## Features
- *Product Recommendations*: Provides recommendations by analyzing product reviews and titles.
- *Natural Language Understanding*: Uses embeddings for similarity search and language models for conversational responses.
- *Customizable Prompt Template*: Easily adaptable to different e-commerce domains.
- *Integrates with AstraDB Vector Store*: Efficient storage and retrieval of vectorized product data.

## Architecture

The eCommerce chatbot is built with the following components:
1. *Data Ingestion*: Reads and processes product data to store as vector embeddings.
2. *Similarity Search*: Searches for relevant products based on customer queries.
3. *Response Generation*: Uses a language model to generate a helpful response based on retrieved information.

This architecture allows for flexible data ingestion, efficient storage and retrieval, and dynamic response generation.

## Setup

### Prerequisites
- Python 
- AstraDB account and access credentials
- OpenAI or Google Generative AI API key for embeddings

### Installation

1. *Clone the Repository*
   ```bash
   git clone https://github.com/VaibhavBomle/eCommerce-chatbot.git
   cd eCommerce-chatbot
