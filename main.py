from fastapi import FastAPI
from routers.agent_router import router as agent_router

app =FastAPI(title = "Autonomous AI Agent",
             description = "An autonomous AI agent that plans tasks, executes them, and generates Word documents.",
             version = "1.0.0")
app.include_router(agent_router)

@app.get("/")
async def home():
    return {"message" : "Welcome to autonomous AI Agent"}

