import asyncio
import os
from dotenv import load_dotenv

# Import BeeAI components
from beeai_framework.agents.requirement import RequirementAgent
from beeai_framework.agents.requirement.requirements.conditional import ConditionalRequirement
from beeai_framework.memory import UnconstrainedMemory
from beeai_framework.backend import ChatModel, ChatModelParameters
from beeai_framework.tools.search.wikipedia import WikipediaTool
from beeai_framework.tools.think import ThinkTool
from beeai_framework.middleware.trajectory import GlobalTrajectoryMiddleware
from beeai_framework.tools import Tool

# Load environment variables
load_dotenv()

async def run_simple_agent():
    print("🚀 Initializing Agent...")
    
    # 1. Check API Key
    model_name = os.getenv("LLM_CHAT_MODEL_NAME", "openai:gpt-4o-mini")
    if not os.getenv("OPENAI_API_KEY") and "openai" in model_name:
        print("❌ CRITICAL: OPENAI_API_KEY is missing in your .env file")
        return

    # 2. Initialize LLM
    try:
        llm = ChatModel.from_name(os.getenv("LLM_CHAT_MODEL_NAME", "openai:gpt-4o-mini"),
        ChatModelParameters(temperature=0)
    )
    except Exception as e:
        print(f"❌ Error loading model. Check your dependencies: {e}")
        return

    # 3. Create a Simple Agent (Wikipedia + Thinking)
    agent = RequirementAgent(
        llm=llm,
        tools=[WikipediaTool(), ThinkTool()],
        memory=UnconstrainedMemory(),
        instructions="You are a helpful assistant. Use tools to answer questions.",
        middlewares=[GlobalTrajectoryMiddleware(included=[Tool])],
        requirements=[
            ConditionalRequirement(ThinkTool, min_invocations=0, max_invocations=2)
        ]
    )

    # 4. Run the Agent
    print("⏳ Agent is thinking...")
    try:
        result = await agent.run("Who is the current president of France?")
        
        # Safe output printing
        if hasattr(result, 'result') and hasattr(result.result, 'text'):
            print(f"\n✅ Answer: {result.result.text}")
        else:
            print(f"\n✅ Answer (Raw): {result}")
            
    except Exception as e:
        print(f"\n🔴 Execution Error: {e}")
        # Check if it's the specific Token error
        if "cache_creation_tokens" in str(e):
            print("\n💡 FIX: This is a library version mismatch.")
            print("Run this command: pip install --upgrade beeai-framework openai pydantic")

if __name__ == "__main__":
    asyncio.run(run_simple_agent())